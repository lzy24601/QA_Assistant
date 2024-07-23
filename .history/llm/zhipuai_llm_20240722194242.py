import os
from typing import Any, Dict, List, Mapping, Optional

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from zhipuai import ZhipuAI


class ZhipuAILLM(LLM):
    model: str = "glm-4"
    temperature: float = 0.1
    api_key: str = None

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any
    ) -> str:
        # 这里会自动获取环境变量中的ZHIPUAI_API_KEY
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
