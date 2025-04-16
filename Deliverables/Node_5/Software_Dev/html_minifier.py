# HTML Minifier - Removes whitespace and comments
import re

def minify_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)  # remove comments
        content = re.sub(r">\s+<", "><", content)  # remove whitespace between tags
        content = re.sub(r"\n+", "", content)  # remove newlines

        with open("minified_output.html", "w", encoding='utf-8') as out:
            out.write(content)

        print("✅ HTML minified to 'minified_output.html'")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    path = input("Enter path to HTML file: ").strip()
    minify_html(path)
