import os
import zhipuai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

zhipuai.api_key = os.environ
