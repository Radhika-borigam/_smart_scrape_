import requests
from bs4 import BeautifulSoup

def fetch_articles(urls):
    articles = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = soup.find_all("p")
                text = " ".join([p.get_text() for p in paragraphs])
                articles.append({"url": url, "content": text[:2000]})  # Limit to 2000 chars
        except Exception as e:
            articles.append({"url": url, "error": str(e)})
    return articles
