## NPC-Forge-Python-Dataset

This repository consolidates ~200,000+ of the best open-source Python programming examples into an organized library of curated solutions purpose-built for the **NPC-Forge** framework. The total number of entries is 43999 with a footprint of around 71,3MB.

[![Size: ~200k+ Samples](https://img.shields.io/badge/Samples-200k+-orange.svg)](#)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

The idea is to use this dataset, originally developed to train LLMs, to provide Python programming abilities to deterministic NPCs. The sheer amount of intents (>43k) and their paraphrases (~4 per intent) makes NPCs surprisingly capable of answering Python related questions.

A lot of work has been done on the original dataset using scripts and local language models:

1. The dataset has been converted to [NDF 0.0 (NPC-Forge Dataset Format)](docs/dataset.md).
2. Removed all duplicated inputs.
3. Pruned inputs to a single line.
4. Removed non-ASCII characters.
5. Lowercased inputs.
6. Added input paraphrases.
7. Removed questions that require code editing (debug this, optimize this, rewrite this).
8. Removed entries containing non functional code.
9. Manual curation, cleanup and enhancement.
10. Added `source` and `license` to track provenance and license of each entry.

The paraphrases generation was done using [granite-4.1 3B](https://www.ibm.com/granite/docs/models/granite4-1) and required around 24 hours of compute on an obsolete machine with 16GB of RAM, Intel i7-4790K CPU and NVIDIA GeForce GTX 1050 Ti.

### Included Datasets

This repository aggregates the following high-quality sources.

| Dataset Name | Entries | Source | Original License |
| :--- | :--- | :--- | :--- | 
| Tested-143k-Python-Alpaca | 8025 | [Vezora (Hugging Face)](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca) | Apache 2.0 |
| self-oss-instruct-sc2-exec-filter-50k | 20459 | [BigCode (Hugging Face)](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2) | ODC-BY |
| Python Functions Reasoning | 2726 | [notbadai (Hugging Face)](https://huggingface.co/datasets/notbadai/python_functions_reasoning) | Apache 2.0 |
| Glaive Python Code QA | 4042 | [thedevastator (Kaggle)](https://www.kaggle.com/datasets/thedevastator/glaive-python-code-qa-dataset) | CC0 1.0 (Public Domain) |
| Python Programming Questions | 8747 | [Bhavesh Mittal (Kaggle)](https://www.kaggle.com/datasets/bhaveshmittal/python-programming-questions-dataset) | CC0 1.0 (Public Domain) |

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
2. **Raw Data:** The datasets contained in the `raw/` directory retain their licenses (Apache 2.0, ODC-BY, CC0). 

*See [`LICENSES.md`](LICENSES.md) for a detailed breakdown of attribution requirements and compatibility.*

---

### Contributing & Credits

Huge thanks to the original creators of these datasets (Vezora, BigCode, notbadai, Bhavesh Mittal, thedevastator) for pushing the boundaries of open-source AI. 

Found a bug in the normalization script? Have a new dataset to add? **Pull requests are welcome!** Please ensure any new datasets added have a permissive license compatible with this repository's goals.

---
*Built with for the NPC-Forge community by Giovanni Blu Mitolo.*
