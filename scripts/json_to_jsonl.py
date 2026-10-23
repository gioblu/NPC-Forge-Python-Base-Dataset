#!/usr/bin/env python3
import os
import json

# Configuration
JSON_DIR = "json"
JSONL_DIR = "jsonl"
OUTPUT_FILE = os.path.join(JSONL_DIR, "dataset_NPC-Forge-Python-Base-Dataset-unified.jsonl")

# Mapping of filename keywords to source and license metadata
# Adjust the keywords if your raw filenames are different
DATASET_METADATA = {
    "dataset_python_ppqd": {"source": "Python Programming Questions Dataset by Bhavesh Mittal", "license": "CC0: Public Domain"},
    "dataset_python-functions-reasoning-100": {"source": "python_functions_reasoning by notbadai", "license": "Apache license 2.0"},
    "dataset_python-glaive-100": {"source": "Glaive Code Assistant dataset by thedevastator", "license": "CC0 1.0 Universal"},
    "dataset_Tested-143k-Python-Alpaca-80": {"source": "Vezora's CodeTester Dataset by Vezora", "license": "Apache license 2.0"},
    "dataset_self-oss-instruct-sc2-exec-filter-50k": {"source": "Final self-alignment training dataset for StarCoder2-Instruct by bigcode", "license": "odc-by Open Data Commons License"},
}

def get_metadata(filename):
    """Determines the source and license based on a filename match."""
    # Strip the .json extension and convert to lowercase for case-insensitive matching
    name_without_ext = os.path.splitext(filename)[0]
    
    # Check for exact match in the dictionary
    if name_without_ext in DATASET_METADATA:
        return DATASET_METADATA[name_without_ext]
        
    # Fallback if no exact match is found
    return {"source": "unknown", "license": "Unknown"}

def unify_json_to_jsonl():
    if not os.path.exists(JSONL_DIR):
        os.makedirs(JSONL_DIR)
        print(f"Created directory: {JSONL_DIR}")

    if not os.path.exists(JSON_DIR):
        print(f"Error: Source directory '{JSON_DIR}' does not exist.")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        count = 0
        
        for filename in sorted(os.listdir(JSON_DIR)):
            if filename.endswith('.json'):
                file_path = os.path.join(JSON_DIR, filename)
                metadata = get_metadata(filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        data = json.load(infile)
                        
                        # Handle list of records
                        if isinstance(data, list):
                            for item in data:
                                if isinstance(item, dict):
                                    # Inject provenance metadata
                                    item["source"] = metadata["source"]
                                    item["license"] = metadata["license"]
                                outfile.write(json.dumps(item, ensure_ascii=False) + '\n')
                                count += 1
                                
                        # Handle single record (dict)
                        elif isinstance(data, dict):
                            data["source"] = metadata["source"]
                            data["license"] = metadata["license"]
                            outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
                            count += 1
                            
                    print(f"Processed: {filename} (Source: {metadata['source']}, License: {metadata['license']})")
                    
                except json.JSONDecodeError:
                    print(f"Skipping file (Invalid JSON): {filename}")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    print(f"\n✅ Successfully unified {count} entries into {OUTPUT_FILE}")

if __name__ == "__main__":
    unify_json_to_jsonl()