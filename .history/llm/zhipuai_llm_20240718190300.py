from email import message
import os

from dotenv import find_dotenv, load_dotenv
from zhipuai import ZhipuAI

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取该 .env 文件，并将其中的环境变量加载到当前的运行环境中
_ = load_dotenv(find_dotenv())

client = ZhipuAI(api_key=os.environ["ZHIPUAI_API_KEY"])

def gen_glm_params(prompt):
    """ 构造GLM模型请求参数 messages
    请求参数：
        prompt:对应的用户提示词
    """
    messages = [{"role": "user", "content": prompt}]
    return messages

def get_completion(prompt, model="glm-4", temperature=0.95):
    """ 获取GLM模型调用结果
    请求参数：
        prompt:对应的提示词
        model:调用的模型，默认为glm-4
        temperature:模型输出的温度系数，控制输出的随机程度，范围(0,1.0]。temperature越低输出内容越一致
    """
    messages = gen_glm_params(prompt)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    if len(response.choices) > 0:
        return response.choices[0].message