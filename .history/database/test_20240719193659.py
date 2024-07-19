import os
import sys

from zhipuai import ZhipuAI
from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import chroma

# 加载api key
_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ['ZHIPIAI_API_KEY']
# 加载PDF
loaders = [PyMuPDFLoader("../data/knowledge_db/pumkin_book/pumpkin_book.pdf")]

docs = []
for loader in loaders:
    docs.extend(loader.load())

# 切分文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
split_docs = text_splitter.split_documents(docs)

# 定义embeddings
client = Z
