from functools import partial
from typing import Dict


LANGS = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "te"]


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict, lang: str) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    string = f"Generate answer in {lang} for the question and output only the answer with no extra information. If the answer is not present in the passage return empty string.\nBased on the given passage:\n{doc['context']}\nQ: {doc['question']}\nA:"

    return string


def doc_to_target(doc: Dict) -> str:
    # Case 1: answers is a dict with 'text' as a list
    if "answers" in doc:
        if isinstance(doc["answers"], dict):
            texts = doc["answers"].get("text", [])
            if texts and isinstance(texts, list):
                return texts[0]
            # Fallback if 'text' is missing or not a list, or empty
            return ""
        else:
            # 'answers' exists but is not a dict: this is likely a data error
            raise TypeError(
                f"Expected 'answers' to be a dict, got {type(doc['answers']).__name__}"
            )
    else:
        # Fallback if answers are missing
        return ""


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
