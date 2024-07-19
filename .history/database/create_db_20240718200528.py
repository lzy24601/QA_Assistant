import chunk
import re

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("data/knowledge_db/pumkin_book/pumpkin_book.pdf")

pages = loader.load()
pdf_page = pages[1]
# print(
#     f"每个元素的类型：{type(pdf_page)}",
#     f"该文档的描述性数据：{pdf_page.metadata}",
#     f"该文档的内容：\n{pdf_page.page_content}",
#     sep="\n-------\n",
# )

pattern = re.compile(r"[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]", re.DOTALL)
pdf_page.page_content = re.sub(
    pattern, lambda match: match.group(0).replace("\n", ""), pdf_page.page_content
)
pdf_page.page_content = pdf_page.page_content.replace("•", "")
pdf_page.page_content = pdf_page.page_content.replace(" ", "")
print(pdf_page.page_content)

CHUNK_SIZE = 500
OVERLAP_SIZE = 50

text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP_SIZE)
text_splitter.split_documents(pdf_page.page_content[0:1000])
split_doc = text_splitter.split_documents()
