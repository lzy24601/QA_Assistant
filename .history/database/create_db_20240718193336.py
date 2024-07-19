from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("data/knowledge_db/pumkin_book/pumpkin_book.pdf")

pages = loader.load()
print(f"{type(pages)},", f"一共{len(pages)}页")
pdf_page = pages[0]
print(f"每个元素的类型：{type(pdf_page)}", f"该文档的描述性数据：", f"该文档的内容：{}", sep="\n-------\n")
