import requests

BACKEND_URL = "http://localhost:8000"

def scrape_articles(urls):
    response = requests.post(f"{BACKEND_URL}/scrape/", json={"urls": urls})
    return response.json() if response.status_code == 200 else None

def query_ai(query):
    response = requests.post(f"{BACKEND_URL}/query/", json={"query": query})
    return response.json() if response.status_code == 200 else None
