# Web Title & Meta Description Fetcher
import requests
from bs4 import BeautifulSoup

def fetch_title_and_meta(url):
    try:
        response = requests.get(url, timeout=8)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No title"
        meta = soup.find("meta", attrs={"name": "description"})
        description = meta["content"].strip() if meta and "content" in meta.attrs else "No meta description"

        print(f"\n📰 Title: {title}")
        print(f"📄 Meta Description: {description}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    url = input("Enter website URL: ").strip()
    fetch_title_and_meta(url)
