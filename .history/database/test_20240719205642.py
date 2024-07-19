import os
import sys

from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from my_embeddings import ZhipuAIEmbeddings
from zhipuai import ZhipuAI

# 加载api key
_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]

# 获取folder_path下所有文件路径，存储在file_paths里
file_paths = []
folder_path = r"data\knowledge_db"
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
print(file_paths)  # ['data/knowledge_db\\pumkin_book\\pumpkin_book.pdf']

# 加载PDF
loaders = [PyMuPDFLoader("../data/knowledge_db/pumkin_book/pumpkin_book.pdf")]

docs = []
for loader in loaders:
    # extend 用于将可迭代对象的所有元素添加到列表中，适合将多个列表合并成一个列表。
    # append 用于将整个对象作为单一元素添加到列表中。
    docs.extend(loader.load())

# 切分文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
split_docs = text_splitter.split_documents(docs)

# 定义embeddings
embedding = ZhipuAIEmbeddings()
# 定义持久化路径
persist_directory = "data/vector_db/chroma"

# 加载向量数据库
vector_db = Chroma.from_documents(
    documents=split_docs, embedding=embedding, persist_directory=persist_directory
)
vector_db.persist()
