import sys
sys.path.append("")
from embedding.my_embeddings import ZhipuAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import find_dotenv, load_dotenv
import os

_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']
