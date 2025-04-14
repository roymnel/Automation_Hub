import json
import os
from datetime import datetime

KEYWORDS_FILE = os.path.join("seo", "keywords.json")
TARGET_DIR = "."  # root of website

def inject_keywords():
    with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
        keywords = json.load(f)

    combined = set()
    for terms in keywords.values():
        combined.update(terms)

    meta_tags = f'<meta name="keywords" content="{", ".join(sorted(combined))}">\n'
    meta_tags += f'<meta name="last-updated" content="{datetime.now().isoformat()}">\n'

    files_updated = 0
    for fname in os.listdir(TARGET_DIR):
        if fname.endswith(".html") and fname not in ["admin.html", "login.html"]:
            path = os.path.join(TARGET_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                if "<meta name=" in line and "keywords" in line:
                    lines[i] = meta_tags
                    break
            else:
                for i, line in enumerate(lines):
                    if "<head>" in line:
                        lines.insert(i + 1, meta_tags)
                        break

            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            files_updated += 1

    print(f"✅ SEO tags updated in {files_updated} files.")

if __name__ == "__main__":
    inject_keywords()
