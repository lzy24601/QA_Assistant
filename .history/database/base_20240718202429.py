import os
import zhipuai
from dotenv import load_dotenv, find_dotenv
from zhipuai_em
_ = load_dotenv(find_dotenv())

zhipuai.api_key = os.environ['ZHIPUAI_API_KEY']

