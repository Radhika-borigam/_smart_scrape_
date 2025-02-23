🚀 Smart Scrape

Smart Scrape is an AI-powered web scraping tool that allows users to extract data from multiple URLs, process it using LLMs (Large Language Models), and store the information in a FAISS vector database. Users can then ask questions, and the system retrieves relevant answers from the stored data.

🔥 Features

➡️ Multi-URL Scraping - Paste multiple URLs, and the system extracts relevant content.➡️ LLM-Powered Processing - Uses OpenAI's embeddings for efficient data representation.➡️ Vector Embedding Storage - Stores extracted data in a FAISS vector database for fast retrieval.➡️ Intelligent Q&A System - Users can ask questions, and the AI retrieves relevant answers from stored content.➡️ FastAPI Backend - Handles scraping, embedding, and retrieval processes.➡️ Streamlit Frontend - Provides a user-friendly interface for interaction.

🏗 Project Structure

SmartScrape/

│── backend/

│   ├── main.py 
                                # FastAPI app
                                
│   ├── scraper.py              # Web scraping logic

│   ├── embeddings.py           # AI embedding & retrieval logic

│   ├── models/

│   │   ├── request_models.py   # Pydantic models

│   ├── vectorstore/            # FAISS index storage

│   ├── utils/

│   │   ├── helpers.py          # Utility functions

│   ├── .env                    # API keys and environment variables

│   ├── requirements.txt        # Dependencies

│
│── frontend/

│   ├── app.py                  # Streamlit frontend

│   ├── utils/

│   │   ├── api.py              # Functions for calling FastAPI endpoints

│   ├── assets/                 # Static files (logos, images)

│   ├── .env                    # Frontend environment variables

│   ├── requirements.txt        # Dependencies


⚡ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Radhika-borigam/SmartScrape.git
cd SmartScrape

2️⃣ Backend Setup (FastAPI)

cd backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

🔗 Backend will be available at: http://localhost:8000🛠 Test API at: http://localhost:8000/docs

3️⃣ Frontend Setup (Streamlit)

cd frontend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

🔗 Frontend will be available at: http://localhost:8501

🎯 Usage Guide

1️⃣ Enter multiple URLs in the frontend.2️⃣ Click 'Scrape' to extract and process content using AI embeddings.3️⃣ Ask questions related to the scraped content.4️⃣ Get relevant answers powered by vector embeddings.

📁 Environment Variables

Create a .env file in both backend/ and frontend/ with:

OPENAI_API_KEY=your_openai_api_key
BACKEND_URL=http://localhost:8000

🛠 Technologies Used

🚀 FastAPI - Backend API💻 Streamlit - Frontend UI📦 FAISS - Vector search storage🧠 LangChain - AI Embeddings & Retrieval🤖 OpenAI - LLM Processing🌎 BeautifulSoup & Requests - Web Scraping

🤝 Contributing

🔹 Feel free to submit issues or contribute to the project!🔹 Fork the repo, make your changes, and submit a PR.

📜 License

🔓 MIT License - You are free to use, modify, and distribute this project.

🚀 Happy Scraping! 🎯

