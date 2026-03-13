from functools import partial
from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    string = f"Are the given two sentences paraphrases of each other?\nAnswer 0 if both are not paraphrases of each other and 1 if the sentences are paraphrases of each other. Output the final answer as Answer: <Answer> where <Answer> is the final answer which is 0/1.\n\nSentence 1: {doc['sentence1']}\nSentence 2: {doc['sentence2']}\nAnswer:"

    return string


def doc_to_choice(doc: Dict, connector: Dict[str, str]) -> list:
    """Convert a XParaphrase-style document into model choice text."""
    question_word = connector["question_word"].strip()
    no = connector["no"].strip()
    yes = connector["yes"].strip()

    return [
        f"{doc['sentence1']}, {question_word}? {no}, {doc['sentence2']}",
        f"{doc['sentence1']}, {question_word}? {yes}, {doc['sentence2']}",
    ]


# -------------------------
# Language words
# -------------------------
LANGUAGES_WORDS = {
    "as": {"question_word": "ঠিকনে", "no": "নহয়", "yes": "হয়"},
    "bn": {"question_word": "ঠিক আছে", "no": "না", "yes": "হ্যাঁ"},
    "gu": {"question_word": "સાચું", "no": "ના", "yes": "હા"},
    "hi": {"question_word": "सही", "no": "नहीं", "yes": "हाँ"},
    "kn": {"question_word": "ಸರಿ", "no": "ಇಲ್ಲ", "yes": "ಹೌದು"},
    "ml": {"question_word": "ശരി", "no": "അല്ല", "yes": "ഉണ്ട്"},
    "mr": {"question_word": "बरोबर", "no": "नाही", "yes": "होय"},
    "or": {"question_word": "ଠିକ୍ କି", "no": "ନାହିଁ", "yes": "ହଁ"},
    "pa": {"question_word": "ਠੀਕ ਹੈ", "no": "ਨਹੀਂ", "yes": "ਹਾਂ"},
    "te": {"question_word": "సరైనదా", "no": "కాదు", "yes": "అవును"},
}


# -------------------------
# Language-specific adapters
# -------------------------
def build_language_fns(base_fn):
    """
    Generate language-specific partial functions for doc_to_specific.
    """
    return {
        lang: partial(base_fn, connector=connector)
        for lang, connector in LANGUAGES_WORDS.items()
    }


# doc_to_choice_* functions
DOC_TO_CHOICE = build_language_fns(doc_to_choice)


for lang in LANGUAGES_WORDS:
    globals()[f"doc_to_choice_{lang}"] = DOC_TO_CHOICE[lang]
