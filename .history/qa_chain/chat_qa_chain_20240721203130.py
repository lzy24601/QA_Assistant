from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


from multiprocessing import context
import sys

sys.path.append("")
import os

from dotenv import find_dotenv, load_dotenv
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from embedding.my_embeddings import ZhipuAIEmbeddings
from llm import zhipuai_llm

_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]
embedding = ZhipuAIEmbeddings()

persist_directory = r'data\vector_db\chroma'
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# print(f"向量库中存储的数量：{vectordb._collection.count()}")
# question = "什么是prompt engineering?"
# docs = vectordb.similarity_search(query=question, k=3)
# for doc in docs:
#     print(doc)

llm = zhipuai_llm(model="glm-4", api_key=zhipuai_api_key)
# print(llm.invoke("你是谁"))

template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。总在回答最后说“谢谢你的提问！”
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate(input_types=["context", "question"], template=template)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever(), return_source_documents=True, chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

retriever = vectordb.as_retriever()

qa = ConversationalRetrievalChain()