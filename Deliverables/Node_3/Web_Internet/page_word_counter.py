# Web Page Word Counter
import requests
from bs4 import BeautifulSoup

def count_words_from_url(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        word_count = len(text.split())
        print(f"📝 Word count for {url}: {word_count} words")
    except Exception as e:
        print("❌ Error fetching page:", e)

if __name__ == "__main__":
    link = input("Enter URL: ").strip()
    count_words_from_url(link)
