import os
import zhipuai import Zhipu
from dotenv import load_dotenv, find_dotenv
from zhipuai_embedding import 
_ = load_dotenv(find_dotenv())

zhipuai.api_key = os.environ['ZHIPUAI_API_KEY']

