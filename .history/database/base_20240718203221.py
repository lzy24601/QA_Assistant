import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = ZhipuAI(api_key=os.environ['ZHIPUAI_API_KEY'])
response = client.embeddings.create(model="embedding-2")

def get_embeddings(query, model="")



query1 = "机器学习"
query2 = "强化学习"
query3 = "大语言模型"
