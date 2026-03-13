from functools import partial
from typing import Dict

import datasets


LANGS = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te", "ur"]


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    prompt = f"Generate answer in {doc.get('lang', '')} for the question and output only the answer with no extra information.\nBased on the given passage:\n{doc.get('context', '')}\nQ: {doc.get('question', '')}\nA:"

    return prompt


def doc_to_target(doc: Dict) -> str:
    return " ".join([ans["text"] for ans in doc.get("answers", []) if "text" in ans])


def process_docs(dataset: datasets.Dataset, lang: str) -> datasets.Dataset:
    # Only filter if language exists AND matches available langs
    if "lang" in dataset.column_names:
        langs_available = set(dataset["lang"])
        if lang in langs_available:
            dataset = dataset.filter(lambda x: x["lang"] == lang)

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
