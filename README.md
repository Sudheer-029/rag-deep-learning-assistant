# RAG-Deep-Learning-Assistant

A **Retrieval-Augmented Generation (RAG)** chatbot built using Wikipedia articles focused on **Deep Learning**.  
Powered by LangChain, ChromaDB, Groq Llama-3, and Gradio.

## 🚀 Features

- Ingests Wikipedia text on topics like Neural Networks, Backpropagation, Gradient Descent.  
- Computes embeddings with `sentence-transformers/all-MiniLM-L6-v2`.  
- Stores vectors in ChromaDB for fast semantic retrieval.  
- Uses Groq’s `llama-3.1-8b-instant` model to generate grounded answers.  
- ChatGPT-style UI via Gradio.  
- Ensures responses rely strictly on retrieved context (and say “I don’t know from the docs” if not).  
- Token-safe retrieval (avoids model limits).

## 🛠️ Installation & Setup

```bash
git clone https://github.com/Sudheer-029/rag-deep-learning-assistant.git
cd rag-deep-learning-assistant
pip install -r requirements.txt
Create a .env file:
GROQ_API_KEY=your_groq_key_here

Usage:
python rag_chat_app.py

Open the displayed URL (http://127.0.0.1:7860 by default) in your browser. Start asking questions like:

What is deep learning?
Explain backpropagation in simple terms.

Project Structure:
.
├── wiki_corpus/           # Raw Wikipedia text files
├── rag_chat_app.py        # Main chat application
├── build_vector_store.py  # Script to generate the vector store
├── requirements.txt
├── .env.example
└── README.md

Data & Vector Store:
wiki_corpus/ includes the raw text from Wikipedia.
chroma_store/ is not included due to size; you can regenerate it using:
python build_vector_store.py

The assistant successfully answers deep-learning domain questions using retrieved context. Example outputs:
Q: What is deep learning and why it is important to know!
Answer: Deep learning is a type of machine learning that focuses on using multilayered neural networks to perform tasks such as classification, regression, and representation learning. These neural networks, inspired by the human brain, are made up of layers of artificial neurons that work together to process and analyze data. The "deep" in deep learning refers to the use of multiple layers, which can range from three to several hundred or thousands, allowing the network to learn complex patterns and relationships in the data. Deep learning has been applied to various fields, including computer vision, speech recognition, natural language processing, and more, and has produced results comparable to and sometimes surpassing human expert performance. Understanding deep learning is important because it has the potential to revolutionize many areas of life, from healthcare and education to finance and transportation, by providing more accurate and efficient solutions to complex problems.




