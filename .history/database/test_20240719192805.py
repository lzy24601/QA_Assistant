import os
import sys

import zhipuai
from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import chroma

_ = load_dotenv(find_dotenv())
zhipuai_api_key = os.