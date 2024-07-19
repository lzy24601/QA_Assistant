import os
import sys

import zhipuai
from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import chroma

# 加载
_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ['ZHIPIAI_API_KEY']

loaders = [PyMuPDFLoader("../data/knowledge_db/pumkin_book/pumpkin_book.pdf")]

docs = []
for loader in loaders:
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)