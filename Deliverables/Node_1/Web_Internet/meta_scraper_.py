# Meta Description Scraper
import requests
from bs4 import BeautifulSoup

def get_meta(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find("meta", attrs={"name": "description"})
        if tag and "content" in tag.attrs:
            print("Meta description:", tag["content"])
        else:
            print("No meta description found.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_meta(input("URL: "))
