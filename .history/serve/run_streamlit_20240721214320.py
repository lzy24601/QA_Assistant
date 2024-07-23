import os
from re import template
import sys
from unittest import result

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm.zhipuai_llm import ZhipuAILLM
from qa_chain.qa_chain import QA_CHAIN_PROMPT

# 添加这个路径的目的是使 Python 能够在该路径下查找并导入模块或包。
sys.path.append()
from dotenv import find_dotenv, load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores.chroma import Chroma

from embedding import my_embeddings

_ = load_dotenv(find_dotenv())

zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]


def generate_response(input_text, api_key):
    llm = ZhipuAILLM()
    output = llm.invoke(input_text)
    output_parser = StrOutputParser()
    output = output_parser.invoke(output)

    return output


def get_vectordb():
    """获取一个向量数据库实例"""

    return vectordb


def get_chat_qa_chain(question: str, api_key: str):
    vectordb = get_vectordb()
    llm = ZhipuAILLM()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectordb.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

    result = qa({"question": question})
    return result['answer']


def get_qa_chain(question: str, api_key: str):
    vectordb = get_vectordb()
    llm = ZhipuAILLM()
    template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
        案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
        {context}
        问题: {question}
        """
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever(), return_source_documents=True, chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    result = qa_chain({"query": question})
    return result["result"]


def main():
    st.title("MY QA ASSISTANT")
    api_key = st.sidebar.text_input()
