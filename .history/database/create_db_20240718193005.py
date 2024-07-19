from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("data/knowledge_db/pumkin_book\pumpkin_book.pdf")

pages = loader.load()
print(f"{type(pages)},", f"一共{len(pages)}页")
