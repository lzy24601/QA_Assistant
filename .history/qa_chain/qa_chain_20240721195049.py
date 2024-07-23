import sys

sys.path.append("")
import os

from dotenv import find_dotenv, load_dotenv
from langchain.vectorstores.chroma import Chroma

from embedding.my_embeddings import ZhipuAIEmbeddings

_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]
embedding = ZhipuAIEmbeddings()

persist_directory = r'data\vector_db\chroma'
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

print(f"向量库中存储的数量：{vectordb._collection.count()}")
question = "什么是prompt engineering?"
docs = vectordb.similarity_search(query=question, k=3)
