## `self-oss-instruct-sc2-exec-filter-50k`

The [self-oss-instruct-sc2-exec-filter-50k](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k) is an exceptional dataset meticulously crafted for training state-of-the-art language models.

The [dataset_self-oss-instruct-sc2-exec-filter-50k](dataset_self-oss-instruct-sc2-exec-filter-50k.json) file contains a cleaned, enhanced and reformatted version of the self-oss-instruct-sc2-exec-filter-50k Dataset designed to be used by NPCs to handle prompts related to Python.

The idea is to use this dataset, originally developed to train LLMs, to provide Python programming abilities to deterministic NPCs. The sheer amount of intents (>10k) and their paraphrases (~4 per intent) makes NPCs surprisingly capable of answering Python related questions.

A lot of work has been done on the original dataset using scripts and local language models:

1. The dataset has been converted to [NDF 0.0 (NPC-Forge Dataset Format)](docs/dataset.md).
2. Removed all duplicated inputs.
3. Pruned inputs to a single line.
4. Removed non-ASCII characters.
5. Lowercased inputs.
6. Added input paraphrases.
7. Removed questions that require code editing (optimize this code, rewrite this code).
8. Moved source code output to `tools` to enable context usage (save it, append it, ecc.).
9. Removed entries containing non functional code.
10. Manual curation, cleanup and enhancement.

The resulting [dataset_self-oss-instruct-sc2-exec-filter-50k](dataset_self-oss-instruct-sc2-exec-filter-50k.json) contains **8777 intents and weights around 10.8MB**. 

### License 

The [dataset_self-oss-instruct-sc2-exec-filter-50k](dataset_self-oss-instruct-sc2-exec-filter-50k.json) file is licensed under [AGPL-3.0](LICENSE).

The [self-oss-instruct-sc2-exec-filter-50k](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k) is licensed under odc-by: Open Data Commons License Attribution family published by bigcode on [huggingface](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k).

