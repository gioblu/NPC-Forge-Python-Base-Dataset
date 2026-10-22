## NPC-Forge-Python-Dataset

This repository consolidates ~200,000+ of the best open-source Python programming examples into an organized library of curated solutions purpose-built for the **NPC-Forge** framework.

[![Size: ~200k+ Samples](https://img.shields.io/badge/Samples-200k+-orange.svg)](#)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

### Included Datasets

This repository aggregates the following high-quality sources.

| Dataset Name | Source | Original License |
| :--- | :--- | :--- |
| Tested-143k-Python-Alpaca | [Vezora (Hugging Face)](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca) | Apache 2.0 |
| self-oss-instruct-sc2-exec-filter-50k | [BigCode (Hugging Face)](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2) | ODC-BY |
| Python Functions Reasoning | [notbadai (Hugging Face)](https://huggingface.co/datasets/notbadai/python_functions_reasoning) | Apache 2.0 |
| Glaive Python Code QA | [thedevastator (Kaggle)](https://www.kaggle.com/datasets/thedevastator/glaive-python-code-qa-dataset) | CC0 1.0 (Public Domain) |
| Python Programming Questions | [Bhavesh Mittal (Kaggle)](https://www.kaggle.com/datasets/bhaveshmittal/python-programming-questions-dataset) | CC0 1.0 (Public Domain) |

---

### Quick Start

#### 1. Clone the Repository
```bash
git clone https://github.com/gioblu/NPC-Forge-Python-Dataset.git
cd NPC-Forge-Python-Dataset
```
*(Note: This repo uses Git LFS for large dataset files. Ensure you have it installed: `git lfs install`)*

#### 2. Normalize and Unify (Optional but Recommended)
If you want to generate the final, optimized, injection-safe dataset from the raw sources, run the normalization script:
```bash
python scripts/normalize_schema.py
```
This will read the `raw/` directory, apply the secure heredoc wrappers, fix language tags, inject provenance metadata, and output a unified file to `processed/unified_agent_v1.jsonl`.

#### 3. Point NPC-Forge to the Dataset
Update your NPC configuration (`config.json`) to point to the processed file:
```json
{
  "optional_datasets": [
    "processed/unified_agent_v1.jsonl"
  ]
}
```

---

### Schema Example

Here is what a processed, agent-ready record looks like. Notice the secure `head` and `tail` injected into the command, and the mandatory provenance tags:

```json
{
  "input": "write a function to find squares of individual elements in a list using lambda function.",
  "tools": [
    {
      "name": "run_in_terminal",
      "arguments": {
        "language": "python",
        "mode": "sync",
        "goal": "Python source code generation",
        "command": "TMP_FILE=$(mktemp /tmp/termy_script_XXXXXX.py) && DELIM=\"__TERMY_BOUNDARY_$$_$RANDOM__\" && cat << \"$DELIM\" > \"$TMP_FILE\"\ndef square_nums(nums):\n    return list(map(lambda x: x ** 2, nums))\n$DELIM\ntermy_set_context 'active_file' \"$TMP_FILE\" && termy_set_context 'active_content' \"$(cat \"$TMP_FILE\")\""
      }
    }
  ],
  "source": "vezora_alpaca_143k",
  "license": "Apache-2.0",
  "permission": "yolo"
}
```

---

### License

This has a **dual-layer licensing model** to respect both open-source software principles and original data creators:

1. **Repository Tooling & Structure:** The normalization scripts, repository structure, and derived formatting are licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.
2. **Raw Data:** The datasets contained in the `raw/` directory retain their original licenses (Apache 2.0, ODC-BY, CC0). 

*See [`LICENSES.md`](LICENSES.md) for a detailed breakdown of attribution requirements and compatibility.*

---

### Contributing & Credits

Huge thanks to the original creators of these datasets (Vezora, BigCode, notbadai, Bhavesh Mittal, thedevastator) for pushing the boundaries of open-source AI. 

Found a bug in the normalization script? Have a new dataset to add? **Pull requests are welcome!** Please ensure any new datasets added have a permissive license compatible with this repository's goals.

---
*Built with for the NPC-Forge community by Giovanni Blu Mitolo.*
