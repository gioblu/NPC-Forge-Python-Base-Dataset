## NPC-Forge-Python-Dataset

This repository consolidates ~43,999 of the best open-source Python programming examples into an organized library of curated solutions purpose-built for the **NPC-Forge** framework. The total number of entries is ~43,999 with a footprint of around 71,3MB.

This dataset, even if originally developed to train LLMs, is now used to provide Python programming abilities to deterministic NPCs. The sheer amount of intents (>43k) and their paraphrases (~4 per intent) makes NPCs surprisingly capable of answering Python related questions.

### Included Datasets

This repository aggregates a curated subset of the following high-quality sources:

| Dataset Name | Entries | Source | Original License |
| :--- | :--- | :--- | :--- | 
| Tested-143k-Python-Alpaca | 8025 | [Vezora (Hugging Face)](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca) | Apache 2.0 |
| self-oss-instruct-sc2-exec-filter-50k | 20459 | [BigCode (Hugging Face)](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2) | ODC-BY |
| Python Functions Reasoning | 2726 | [notbadai (Hugging Face)](https://huggingface.co/datasets/notbadai/python_functions_reasoning) | Apache 2.0 |
| Glaive Python Code QA | 4042 | [thedevastator (Kaggle)](https://www.kaggle.com/datasets/thedevastator/glaive-python-code-qa-dataset) | CC0 1.0 (Public Domain) |
| Python Programming Questions | 8747 | [Bhavesh Mittal (Kaggle)](https://www.kaggle.com/datasets/bhaveshmittal/python-programming-questions-dataset) | CC0 1.0 (Public Domain) |

A lot of work has been done on the original dataset using scripts and local language models:

1. The dataset has been converted to [NDF 0.0 (NPC-Forge Dataset Format)](docs/dataset.md).
2. Removed all inputs longer than 100 characters.
3. Removed all duplicated inputs.
4. Removed questions that require code editing (debug this, optimize this, rewrite this).
5. Removed entries containing non functional code.
6. Removed non-ASCII characters.
7. Lowercased inputs.
8. Added at least 4 input paraphrases per entry.
9. Manual curation, cleanup and enhancement.
10. Added `source` and `license` to track provenance and license of each entry.

The paraphrases generation was done using [granite-4.1 3B](https://www.ibm.com/granite/docs/models/granite4-1) and required around 24 hours of compute on an obsolete machine with 16GB of RAM, Intel i7-4790K CPU and NVIDIA GeForce GTX 1050 Ti.

---

### Schema Example

Here is what a processed, agent-ready record looks like. Notice the secure `head` and `tail` injected into the command, and the mandatory provenance tags:

```json
{
    "input": [
        "explain how to convert a numpy array into a list format using python",
        "create a python snippet to convert numpy array to list",
        "convert numpy array to list in python"
    ],
    "output": "<||completion||>\n\nCertainly! To convert a...",
    "permission": "yolo",
    "tools": [
        {
            "name": "run_in_terminal",
            "arguments": {
                "command": "import numpy as np \n...",
                "explanation": "Writes Python script in a temp file and updates context.",
                "goal": "Python source code generation",
                "mode": "sync",
                "language": "py"
            }
        }
    ],
    "source": "Vezora's CodeTester Dataset by Vezora",
    "license": "Apache license 2.0"
}
```

---

### License

Dual-layer licensing is applied to respect both open-source software principles and original data creators:

1. **Repository Tooling & Structure:** The normalization scripts, repository structure, and derived formatting are licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.
2. **Raw Data:** The datasets contained in the `raw/` directory retain their licenses (Apache 2.0, ODC-BY, CC0). 

*See [`LICENSES.md`](LICENSES.md) for a detailed breakdown of attribution requirements and compatibility.*

---

### Contribute

Huge thanks to the original creators of these datasets (Vezora, BigCode, notbadai, Bhavesh Mittal, thedevastator) for pushing the boundaries of open-source AI. 

Have a new dataset to add? **Pull requests are welcome!** Please ensure any new datasets added have a permissive license compatible with this repository's goals.

---
*Built with for the NPC-Forge community by Giovanni Blu Mitolo.*
