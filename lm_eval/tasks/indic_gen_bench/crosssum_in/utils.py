from functools import partial
from typing import Dict

import datasets


LANGS = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te", "ur"]


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    prompt = f"Summarize the following article: {doc['text']}\nSummary:"

    return prompt


def process_docs(dataset: datasets.Dataset, lang: str) -> datasets.Dataset:
    """
    Filter a dataset by language.

    If the dataset contains nested 'examples', they are flattened
    before applying the language filter.
    """

    def _filter_fn(row):
        return row.get("lang") == lang

    # Case 1: dataset already has flat language rows
    if "lang" in dataset.column_names:
        return dataset.filter(_filter_fn)

    # Case 2: dataset contains nested examples that need flattening
    if "examples" in dataset.column_names:
        dataset = dataset.map(
            lambda batch: {
                key: [ex[key] for ex in batch["examples"]]
                for key in batch["examples"][0]
            },
            batched=True,
            remove_columns=[
                col for col in ("examples", "canary") if col in dataset.column_names
            ],
        )
        return dataset.filter(_filter_fn)

    # Fallback: return dataset unchanged if schema is unexpected
    return dataset


# -------------------------
# Language-specific adapters
# -------------------------
def build_language_fns(base_fn):
    """
    Generate language-specific partial functions for process_docs.
    """
    return {lang: partial(base_fn, lang=lang) for lang in LANGS}


# process_docs_* functions
process_doc_fns = build_language_fns(process_docs)


for lang in LANGS:
    globals()[f"process_docs_{lang}"] = process_doc_fns[lang]
