from langchain_community.embeddings import HuggingFaceEmbeddings

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vec = emb.embed_query("Hello world")
print("Embedding length:", len(vec))
