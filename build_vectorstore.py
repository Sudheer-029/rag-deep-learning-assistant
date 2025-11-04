import os
import glob
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# Path where your .txt files are stored
DATA_DIR = "./wiki_corpus"

# Load chunks
docs = []
for filepath in glob.glob(f"{DATA_DIR}/*.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        docs.append(Document(page_content=text, metadata={"source": filepath}))

print(f"Loaded {len(docs)} documents")

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create Chroma DB
db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_store"
)

db.persist()
print("✅ Chroma vector DB created & saved to ./chroma_store")
