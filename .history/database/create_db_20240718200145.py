import re

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
loader = PyMuPDFLoader("data/knowledge_db/pumkin_book/pumpkin_book.pdf")

pages = loader.load()
print(f"{type(pages)},", f"一共{len(pages)}页")
pdf_page = pages[1]
print(
    f"每个元素的类型：{type(pdf_page)}",
    f"该文档的描述性数据：{pdf_page.metadata}",
    f"该文档的内容：\n{pdf_page.page_content}",
    sep="\n-------\n",
)

pattern = re.compile(r"[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]", re.DOTALL)
pdf_page.page_content = re.sub(
    pattern, lambda match: match.group(0).replace("\n", ""), pdf_page.page_content
)
pdf_page.page_content = pdf_page.page_content.replace('•', '')
pdf_page.page_content = pdf_page.page_content.replace(' ', '')
print(pdf_page.page_content)

CHUNK_SIZE = 500
