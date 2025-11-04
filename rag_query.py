from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load Chroma DB
db = Chroma(
    embedding_function=embeddings,
    persist_directory="./chroma_store"
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# Initialize Groq LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI that answers questions using provided context.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
""")

def rag_query(question):
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content[:500] for d in docs])

    chain = prompt | llm
    answer = chain.invoke({"context": context, "question": question})
    
    print("\n🔎 **Retrieved Documents:**")
    for d in docs:
        print(" -", d.metadata["source"])

    print("\n🤖 **Answer:**")
    print(answer.content)

# Test query
rag_query("What is backpropagation in deep learning?")
