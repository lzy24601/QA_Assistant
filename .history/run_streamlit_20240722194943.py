import os

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.vectorstores.chroma import Chroma
from langchain_core.output_parsers import StrOutputParser

from embedding import my_embeddings
from llm.zhipuai_llm import ZhipuAILLM

_ = load_dotenv(find_dotenv())

zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]


def generate_response(input_text, api_key):
    llm = ZhipuAILLM(api_key=api_key)
    output = llm.invoke(input_text)
    output_parser = StrOutputParser()
    output = output_parser.invoke(output)

    return output


def get_vectordb():
    """获取一个向量数据库"""

    # 获取用于embedding的实例
    embedding = my_embeddings.ZhipuAIEmbeddings()
    persist_directory = r'data\vector_db\chroma'
    vectordb = 

    return vectordb


def get_chat_qa_chain(question: str, api_key: str):
    vectordb = get_vectordb()
    llm = ZhipuAILLM()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectordb.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

    result = qa({"question": question})
    return result["answer"]


def get_qa_chain(question: str, api_key: str):
    vectordb = get_vectordb()
    llm = ZhipuAILLM()
    template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
        案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
        {context}
        问题: {question}
        """
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"], template=template
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    result = qa_chain({"query": question})
    return result["result"]


def main():
    st.title("MY QA ASSISTANT")
    api_key = st.sidebar.text_input("api_key", type="password")

    select_method = st.radio(
        "你想选择那种模式对话？",
        ["None", "qa_chain", "chat_qa_chain"],
        captions=["1", "2", "3"],
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "text": prompt})

        if select_method == "None":
            answer = generate_response(prompt, api_key)
        elif select_method == "qa_chain":
            answer = get_qa_chain(prompt, api_key)
        elif select_method == "chat_qa_chain":
            answer = get_chat_qa_chain(prompt, api_key)

        if answer is not None:
            st.session_state.messages.append({"role": "assistant", "text": answer})

        for message in st.session_state.messages:
            if message["role"] == "user":
                messages.chat_message("user").write(message["text"])
            elif message["role"] == "assistant":
                messages.chat_message("assistant").write(message["text"])


if __name__ == "__main__":
    # main()
    print(generate_response("你是谁？", zhipuai_api_key))
