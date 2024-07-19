from langchain.vectorstores import chroma
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import zhipuai
import os
from dotenv import find_dotenv