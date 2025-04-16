# File Line Counter - Counts lines in any file
def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        print(f"📄 {file_path} has {len(lines)} lines.")
    except Exception as e:
        print("❌ Error reading file:", e)

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    count_lines(path)
