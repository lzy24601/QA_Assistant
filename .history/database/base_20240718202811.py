import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

zhipuai.api_key = os.environ['ZHIPUAI_API_KEY']
client =
