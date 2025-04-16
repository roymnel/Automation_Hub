# HTTP Status Code Checker
import requests

def check_status(url):
    try:
        response = requests.head(url, timeout=5)
        print(f"🔍 {url} returned status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error checking {url}:", e)

if __name__ == "__main__":
    url = input("Enter URL to check (include http/https): ").strip()
    check_status(url)
