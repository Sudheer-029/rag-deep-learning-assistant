import os
from dotenv import load_dotenv
import gradio as gr
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load key
load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("❌ Add GROQ_API_KEY in your .env file!")

# Embeddings + Vector DB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_store", embedding_function=embedding_model)
retriever = db.as_retriever(search_kwargs={"k": 2})  # token safe

# Groq LLM
llm = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

# ✅ Your custom journalist prompt
system_prompt = """
You are an AI communicator writing for a general public audience interested in technology and innovation.

Your task:
Write a summary/explanation based on the retrieved context.

Rules:
- One paragraph, ~80–120 words
- No bullet points or sections
- Plain language
- Friendly and clear
- Avoid hype words (transformative, game-changer)
- Avoid academic tone (delves into, leverages)
- Avoid clichés (ushering in a new era)
- Avoid semicolons and long sentences

Goal:
Help a curious non-expert understand the topic in simple language.

Context you MUST use:
{context}

User Question:
{question}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{question}")
])

def rag_chat(message, history):
    try:
        docs = retriever.invoke(message)

        # Limit each chunk to avoid 413 error
        trimmed = [d.page_content[:2000] for d in docs]
        context = "\n\n".join(trimmed)

        chain = prompt | llm | parser
        answer = chain.invoke({"context": context, "question": message})

        return answer
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Using UI similar to ChatGPT
chat_ui = gr.ChatInterface(
    fn=rag_chat,
    title="📚 Wikipedia RAG Chatbot",
    description="Ask about deep learning / AI topics — powered by custom Wikipedia embeddings",
    theme="default",
)

chat_ui.launch(share=True)
