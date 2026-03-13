from functools import partial
from typing import Dict

import datasets


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict, lang: str) -> str:
    string = f"To {lang}: {doc['source']}\nOutput: "
    return string.strip()


def process_docs(
    dataset: datasets.Dataset, translation_direction: str, lang: str
) -> datasets.Dataset:
    """
    Filter and normalize a dataset by translation direction and language.

    If the dataset contains an 'examples' column, it is flattened before filtering.
    """

    def _filter_fn(row):
        return (
            row.get("translation_direction") == translation_direction
            and row.get("lang") == lang
        )

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
# Languages
# -------------------------
LANGS = {
    "as": "Assamese",
    "bn": "Bengali",
    "en": "English",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "or": "Odia",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
}


# -------------------------
# Language-specific adapters
# -------------------------
def build_doc_to_text_fns(base_fn):
    """
    Generate language-specific doc_to_text functions.
    """
    return {lang: partial(base_fn, lang=lang) for lang in LANGS}


def build_process_docs_fns(base_fn):
    """
    Generate language-pair-specific process_docs functions.

    Skips English-only pairs.
    """
    fns = {}

    for lang in LANGS:
        if lang == "en":
            continue

        fns[f"{lang}_en"] = partial(base_fn, translation_direction="xxen", lang=lang)
        fns[f"en_{lang}"] = partial(base_fn, translation_direction="enxx", lang=lang)

    return fns


# -------------------------
# Build adapters
# -------------------------
DOC_TO_TEXT = build_doc_to_text_fns(doc_to_text)
PROCESS_DOCS = build_process_docs_fns(process_docs)


# -------------------------
# Export globals for lm-eval
# -------------------------
for lang in LANGS:
    if lang == "en":
        continue

    globals()[f"doc_to_text_{lang}_en"] = DOC_TO_TEXT[lang]
    globals()[f"doc_to_text_en_{lang}"] = DOC_TO_TEXT["en"]
    globals()[f"process_docs_{lang}_en"] = PROCESS_DOCS[f"{lang}_en"]
    globals()[f"process_docs_en_{lang}"] = PROCESS_DOCS[f"en_{lang}"]
