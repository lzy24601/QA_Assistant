import os
import zhipuai
from dotenv import load_dotenv, find_dotenv
from zhipuai
_ = load_dotenv(find_dotenv())

zhipuai.api_key = os.environ['ZHIPUAI_API_KEY']

