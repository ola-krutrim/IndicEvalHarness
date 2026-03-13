from functools import partial
from typing import Dict

import datasets


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict, lang: str) -> str:
    string = f"Generate answer in {LANGS[lang]} for the question and output only the answer with no extra information.\nBased on the given passage:\n{doc.get('context', '')}\nQ: {doc.get('question', '')}\nA:"

    return string


def _extract_answer_text(answer_field) -> str:
    """
    Extract text from XORQA-style answers:
    List[{ "text": str, "answer_start": int }]
    """
    if not answer_field:
        return "[NO_ANSWER]"

    if isinstance(answer_field, list):
        return " ".join(
            ans["text"]
            for ans in answer_field
            if isinstance(ans, dict) and ans.get("text")
        )

    return "[NO_ANSWER]"


def doc_to_target_en(doc: Dict) -> str:
    return _extract_answer_text(doc.get("answers"))


def doc_to_target_xx(doc: Dict) -> str:
    return _extract_answer_text(doc.get("translated_answers"))


def process_docs(dataset: datasets.Dataset, lang: str) -> datasets.Dataset:
    # Only filter if language exists AND matches available langs
    if "lang" in dataset.column_names:
        langs_available = set(dataset["lang"])
        if lang in langs_available:
            dataset = dataset.filter(lambda x: x["lang"] == lang)

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
}


# -------------------------
# Language-specific adapters
# -------------------------
def build_fns(base_fn):
    """
    Generate language-specific functions.
    """
    return {lang: partial(base_fn, lang=lang) for lang in LANGS}


# -------------------------
# Build adapters
# -------------------------
DOC_TO_TEXT = build_fns(doc_to_text)
PROCESS_DOCS = build_fns(process_docs)


# -------------------------
# Export globals for lm-eval
# -------------------------
for lang in LANGS:
    if lang == "en":
        continue

    globals()[f"doc_to_text_{lang}_en"] = DOC_TO_TEXT["en"]
    globals()[f"doc_to_text_{lang}"] = DOC_TO_TEXT[lang]
    globals()[f"process_docs_{lang}"] = PROCESS_DOCS[lang]
