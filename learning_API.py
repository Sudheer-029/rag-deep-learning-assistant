'''
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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"
)

response = llm.invoke("Explain vector databases in one paragraph")
print(response)
'''

from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Now you can use the environment variable
llm = ChatGroq(model="llama-3.1-8b-instant")  # Will automatically pick up GROQ_API_KEY

response = llm.invoke("What is agentic AI?")
print(response.content)
