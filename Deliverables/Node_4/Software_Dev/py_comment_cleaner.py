# Python File Comment Cleaner
# Removes all comments from a .py script (lines starting with #)

def remove_comments(file_path):
    try:
        with open(file_path, 'r') as src, open("no_comments.py", 'w') as out:
            for line in src:
                stripped = line.strip()
                if stripped.startswith("#") or stripped == "":
                    continue
                out.write(line)
        print("✅ Output saved to 'no_comments.py'")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    path = input("Enter Python file path: ").strip()
    remove_comments(path)
