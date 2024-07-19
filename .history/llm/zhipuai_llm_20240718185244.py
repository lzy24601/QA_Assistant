import os

from dotenv import find_dotenv, load_dotenv
from zhipuai import ZhipuAI

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取该 .env 文件，并将其中的环境变量加载到当前的运行环境中
_ = load_dotenv(find_dotenv())

client = ZhipuAI(api_key=os.environ["ZHIPUAI_API_KEY"])

def gen_glm_params(prompt):
    """  """