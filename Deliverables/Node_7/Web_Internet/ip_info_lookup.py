# IP Information Lookup using ipinfo.io API (no key required for basic use)
import requests

def lookup_ip(ip=""):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=5)
        data = response.json()
        print("\n🌐 IP Info:")
        for key, value in data.items():
            print(f"  {key.title()}: {value}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    ip = input("Enter IP address (or leave blank for your own): ").strip()
    lookup_ip(ip)
