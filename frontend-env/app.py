import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Backend URL
BACKEND_URL = "http://localhost:8000"

# Streamlit UI
st.title("Smart Scrape: AI-Powered News Research 📈")
st.sidebar.title("Enter News Article URLs")

# Input URLs
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# Button to send URLs to backend for processing
if st.sidebar.button("Process URLs"):
    urls = [url for url in urls if url]  # Remove empty URLs
    if urls:
        response = requests.post(f"{BACKEND_URL}/scrape/", json={"urls": urls})
        if response.status_code == 200:
            st.success("✅ Scraping and embedding completed!")
        else:
            st.error(f"⚠️ Error: {response.json()['detail']}")
    else:
        st.warning("⚠️ Please enter at least one URL.")

# Query input
query = st.text_input("Ask a question about the articles:")

# Send query to FastAPI and display the result
if query:
    response = requests.post(f"{BACKEND_URL}/query/", json={"query": query})
    if response.status_code == 200:
        result = response.json()
        st.subheader("💡 Answer")
        st.write(result["answer"])

        # Display sources
        if result.get("sources"):
            st.subheader("📌 Sources:")
            sources_list = result["sources"].split("\n")
            for source in sources_list:
                st.write(f"- {source}")
    else:
        st.error(f"⚠️ Error: {response.json()['detail']}")
