# Licensing and Attribution

This repository (`NPC-Forge-Python-Dataset`) is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**. This license applies to the repository structure, normalization scripts, tooling, and any derived formatting or structural modifications made to the data.

However, this repository contains third-party datasets that retain their original, highly permissive licenses. The AGPLv3 license does not override or restrict the original licenses of the raw data files contained in the `raw/` directory. 

By using this repository, you agree to comply with the AGPLv3 for the tooling/scripts, and the respective licenses for the data.

## Original Dataset Licenses

### 1. Tested-143k-Python-Alpaca
- **Source:** [Vezora (Hugging Face)](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca)
- **License:** Apache License 2.0

### 2. self-oss-instruct-sc2-exec-filter-50k
- **Source:** [BigCode (Hugging Face)](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2)
- **License:** Open Data Commons Attribution License (ODC-BY)
- **Attribution Requirement:** You must give appropriate credit to BigCode. *Note: Our processing scripts automatically inject a `"source": "bigcode_self_oss"` tag into each record to fulfill this requirement.*

### 3. Python Functions Reasoning
- **Source:** [notbadai (Hugging Face)](https://huggingface.co/datasets/notbadai/python_functions_reasoning)
- **License:** Apache License 2.0

### 4. Python Programming Questions Dataset
- **Source:** [Bhavesh Mittal (Kaggle)](https://www.kaggle.com/datasets/bhaveshmittal/python-programming-questions-dataset)
- **License:** CC0 1.0 Universal (Public Domain)

### 5. Glaive Python Code QA Dataset
- **Source:** [thedevastator (Kaggle)](https://www.kaggle.com/datasets/thedevastator/glaive-python-code-qa-dataset)
- **License:** CC0 1.0 Universal (Public Domain)

---

### Summary for Users
- **Can I use this for commercial purposes?** Yes. All underlying data licenses permit commercial use, and the AGPLv3 allows commercial use as long as you comply with its source-disclosure requirements for any modified software/tooling you distribute.
- **Do I need to provide attribution?** Yes, for the ODC-BY dataset. This is automatically handled if you use the `processed/` datasets, as they contain the required `"source"` metadata tags.
