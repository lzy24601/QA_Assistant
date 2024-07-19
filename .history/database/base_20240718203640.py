import os

from dotenv import find_dotenv, load_dotenv
from zhipuai import ZhipuAI

_ = load_dotenv(find_dotenv())

client = ZhipuAI(api_key=os.environ["ZHIPUAI_API_KEY"])
response = client.embeddings.create(model="embedding-2")


def get_embeddings(query, model="embedding-2"):
    response = client.embeddings.create(model="embedding-2", query=query)

    return response.data.embedding


query1 = "机器学习"
query2 = "强化学习"
query3 = "大语言模型"
emb1 = get_embeddings(quer)
