# JSON Pretty Printer
import json

def pretty_print_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        pretty = json.dumps(data, indent=4)
        print("\nFormatted JSON Output:\n")
        print(pretty)
        with open("pretty_output.json", "w") as out:
            out.write(pretty)
        print("\n✅ Output saved as 'pretty_output.json'")
    except Exception as e:
        print("❌ Error reading JSON file:", e)

if __name__ == "__main__":
    path = input("Enter path to .json file: ").strip()
    pretty_print_json(path)
