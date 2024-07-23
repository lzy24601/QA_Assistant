import os
import sys

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm.zhipuai_llm import ZhipuAILLM

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
    retriever = vectordb.as_