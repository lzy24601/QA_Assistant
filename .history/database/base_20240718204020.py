import os
import n
from dotenv import find_dotenv, load_dotenv
from zhipuai import ZhipuAI

_ = load_dotenv(find_dotenv())

client = ZhipuAI(api_key=os.environ["ZHIPUAI_API_KEY"])


def get_embeddings(query, model="embedding-2"):
    response = client.embeddings.create(input=query, model="embedding-2")

    return response.data[0].embedding


query1 = "机器学习"
query2 = "强化学习"
query3 = "大语言模型"
emb1 = get_embeddings(query1)
print(emb1)
