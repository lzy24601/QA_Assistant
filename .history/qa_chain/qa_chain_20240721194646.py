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
vector