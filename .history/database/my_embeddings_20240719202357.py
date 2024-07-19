from __future__ import annotations
import logging
from typing import Any, Dict, List
from venv import logger
from langchain.embeddings.base import Embeddings
from langchain.pydantic_v1 import BaseModel, root_validator

logger