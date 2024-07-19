import os
from email import message
from typing import Any, Dict, List, Mapping, Optional

from dotenv import find_dotenv, load_dotenv
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.callbacks.manager import CallbackManagerForChainRun
from langchain_core.language_models.llms import LLM
from zhipuai import ZhipuAI

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取该 .env 文件，并将其中的环境变量加载到当前的运行环境中
# _ = load_dotenv(find_dotenv())

# client = ZhipuAI(api_key=os.environ["ZHIPUAI_API_KEY"])


# def gen_glm_params(prompt):
#     """构造GLM模型请求参数 messages
#     请求参数：
#         prompt:对应的用户提示词
#     """
#     messages = [{"role": "user", "content": prompt}]
#     return messages


# def get_completion(prompt, model="glm-4", temperature=0.95):
#     """获取GLM模型调用结果
#     请求参数：
#         prompt:对应的提示词
#         model:调用的模型,默认为glm-4
#         temperature:模型输出的温度系数，控制输出的随机程度，范围(0,1.0]。temperature越低输出内容越一致
#     """
#     messages = gen_glm_params(prompt)
#     response = client.chat.completions.create(
#         model=model, messages=messages, temperature=temperature
#     )
#     if len(response.choices) > 0:
#         return response.choices[0].message.content
#     return "generate answer error"


# print(get_completion("你好"))
class ZhipuAILLM(LLM):
    _ = load_dotenv(find_dotenv())
    model: str = "glm-4"
    temperature: float = 0.1
    api_key: str = os.environ[]


    def _call(
        self,
        prompt: str,
        stop: List[str] | None = None,
        run_manager: CallbackManagerForLLMRun | None = None,
        **kwargs: Any
    ) -> str:
        client = ZhipuAI(api_key=self.api_key)

        def gen_glm_params(prompt):
            messages = [{"role": "user", "content": prompt}]
            return messages

        messages = gen_glm_params(prompt)
        response = client.chat.completions.create(
            model=self.model, messages=messages, temperature=self.temperature
        )

        if len(response.choices) > 0:
            return response.choices[0].message.content
        return "generate answer error"

    @property
    def _default_params(self) -> Dict[str, Any]:
        """获取调用API的默认参数"""
        normal_params = {
            "temperature": self.temperature,
        }
        return {**normal_params}

    @property
    def _llm_type(self) -> str:
        return "Zhipu"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {**{"model": self.model}, **self._default_params}
