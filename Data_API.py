from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Now you can use the environment variable
llm = ChatGroq(model="llama-3.1-8b-instant")  # Will automatically pick up GROQ_API_KEY

response = llm.invoke("What is agentic AI?")
print(response.content)

