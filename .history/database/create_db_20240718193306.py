from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("data/knowledge_db/pumkin_book/pumpkin_book.pdf")

pages = loader.load()
print(f"{type(pages)},", f"一共{len(pages)}页")
pdf_page = pages[0]
print(f"每个元素的类型：{type(pdf_page)}", f"gai'wen'dang", f"", sep="\n-------\n")
