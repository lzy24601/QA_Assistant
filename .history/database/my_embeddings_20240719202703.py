from __future__ import annotations
import logging
from typing import Any, Dict, List
from langchain.embeddings.base import Embeddings
from langchain.pydantic_v1 import BaseModel, root_validator

logger = logging.getLogger(__name__)

class ZhipuAIEmbeddings(BaseModel, Embeddings):
    """ 智谱ai embedding模型 """

    client: Any

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """ 实例化Zhipu """
