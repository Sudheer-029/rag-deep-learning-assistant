import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = "./wiki_corpus"

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

all_chunks = []

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        path = os.path.join(DATA_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        chunks = text_splitter.split_text(text)
        all_chunks.extend(chunks)
        
        print(f"{filename}: {len(chunks)} chunks")

print(f"\nTotal chunks: {len(all_chunks)}")
# Optionally, save all chunks to a single file for verification