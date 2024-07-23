import streamlit as st
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import sys

from llm.zhipuai_llm import ZhipuAILLM
# 添加这个路径的目的是使 Python 能够在该路径下查找并导入模块或包。
sys.path.append()
from embedding import my_embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']

def generate_response(input_text, api_key):
    llm = ZhipuAILLM()
    output = llm.invoke(input_text)
    output_parser = StrOutputParser()
    