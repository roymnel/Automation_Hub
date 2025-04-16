# Website Response Time Checker
import requests
import time

def check_response_time(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()
        duration = end - start
        print(f"\n🌐 {url}")
        print(f"🔁 Status Code: {response.status_code}")
        print(f"⏱️ Response Time: {duration:.2f} seconds")
    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    url = input("Enter website URL: ").strip()
    check_response_time(url)
