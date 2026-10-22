import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DIR = os.path.abspath(os.path.join(BASE_DIR, '../json'))
JSONL_DIR = os.path.abspath(os.path.join(BASE_DIR, '../jsonl'))
OUTPUT_FILE = os.path.join(JSONL_DIR, 'NPC-Forge-Python-Base-Dataset-unified.jsonl')

def unify_json_to_jsonl():
    if not os.path.exists(JSONL_DIR):
        os.makedirs(JSONL_DIR)
        print(f"Created directory: {JSONL_DIR}")

    if not os.path.exists(JSON_DIR):
        print(f"Error: Source directory '{JSON_DIR}' does not exist.")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        count = 0
        
        def write_to_jsonl(data):
            nonlocal count
            if isinstance(data, list):
                for item in data:
                    outfile.write(json.dumps(item, ensure_ascii=False) + '\n')
                    count += 1
            else:
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
                count += 1

        for filename in sorted(os.listdir(JSON_DIR)):
            if filename.endswith('.json'):
                file_path = os.path.join(JSON_DIR, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        data = json.load(infile)
                        write_to_jsonl(data)
                        print(f"Processed: {filename}")
                except json.JSONDecodeError:
                    print(f"Skipping file (Invalid JSON): {filename}")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    print(f"\nDone! Created '{OUTPUT_FILE}' with {count} total rows.")

if __name__ == '__main__':
    unify_json_to_jsonl()
