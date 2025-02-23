import os
import pickle
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS  # Updated import
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.llms import OpenAI  # Updated import
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File to store embeddings
VECTORSTORE_PATH = "vectorstore/faiss_store.pkl"

# Load or create vector store
def load_vectorstore(docs):
    if os.path.exists(VECTORSTORE_PATH):
        with open(VECTORSTORE_PATH, "rb") as f:
            return pickle.load(f)
    else:
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = FAISS.from_documents(docs, embeddings)
        with open(VECTORSTORE_PATH, "wb") as f:
            pickle.dump(vectorstore, f)
        return vectorstore

def process_query(query):
    # Load stored FAISS index
    if os.path.exists(VECTORSTORE_PATH):
        with open(VECTORSTORE_PATH, "rb") as f:
            vectorstore = pickle.load(f)
        retriever = vectorstore.as_retriever()
        llm = OpenAI(openai_api_key=OPENAI_API_KEY)
        chain = RetrievalQAWithSourcesChain.from_llm(llm, retriever=retriever)
        result = chain({"question": query}, return_only_outputs=True)
        return {"answer": result["answer"], "sources": result.get("sources", "")}
    return {"answer": "No data available. Please process URLs first.", "sources": ""}
