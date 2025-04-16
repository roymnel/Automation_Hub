# Link Checker - Validates all hyperlinks in a given HTML file
import re
import requests

def check_links(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as file:
            content = file.read()
        links = re.findall(r'href=[\'"]?([^\'" >]+)', content)
        print(f"🔗 Found {len(links)} links.")
        for link in links:
            if not link.startswith("http"):
                print(f"Skipping non-HTTP link: {link}")
                continue
            try:
                r = requests.head(link, allow_redirects=True, timeout=5)
                status = r.status_code
                print(f"{link} → HTTP {status}")
            except Exception as e:
                print(f"{link} → ❌ Failed ({e})")
    except Exception as e:
        print("Error reading HTML file:", e)

if __name__ == "__main__":
    file = input("Enter path to HTML file: ").strip()
    check_links(file)
