import re
from functools import partial
from typing import Dict


LANGS = ["bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict, lang: str) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    prompt = (
        f"Generate answer in English for the question in {lang}.\n{doc['question']}\nA:"
    )

    return prompt


def doc_to_target(doc: Dict) -> str:
    text = doc.get("answer", "")
    match = re.search(r"####\s*(\d+)", text)

    return match.group(1) if match else ""


# -------------------------
# Language-specific adapters
# -------------------------
def build_language_fns(base_fn):
    """
    Generate language-specific partial functions for doc_to_specific.
    """
    return {lang: partial(base_fn, lang=lang) for lang in LANGS}


# doc_to_text_* functions
DOC_TO_TEXT = build_language_fns(doc_to_text)


for lang in LANGS:
    globals()[f"doc_to_text_{lang}"] = DOC_TO_TEXT[lang]
