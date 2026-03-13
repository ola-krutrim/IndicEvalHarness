from functools import partial
from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict, connector: Dict[str, str]) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    string = f"What is the sentiment of the given text?\nAnswer 0 if the sentiment is positive and 1 if the sentiment is negative. Output the final answer as Answer: <Answer> where <Answer> is the final answer which is 0/1.\n\nText: {doc['INDIC REVIEW']}\n{connector['question_word']}\nAnswer:"

    return string


def doc_to_choice(doc: Dict, connector: Dict[str, str]) -> list:
    question_word = connector["question_word"].strip()
    positive = connector["positive"].strip()
    negative = connector["negative"].strip()

    return [
        f"{doc['INDIC REVIEW']}, {question_word}? {positive}",
        f"{doc['INDIC REVIEW']}, {question_word}? {negative}",
    ]


def doc_to_target(doc: Dict) -> int:
    try:
        label = doc["LABEL"].strip().lower()
        if label == "positive":
            return 0
        elif label == "negative":
            return 1
    except ValueError:
        # Some of the entries have None as label.
        return 0


# -------------------------
# Language words
# -------------------------
LANGUAGES_WORDS = {
    "as": {"question_word": "ভাব", "positive": "ধনাত্মক", "negative": "ঋণাত্মক"},
    "bn": {"question_word": "অনুভূতি", "positive": "ইতিবাচক", "negative": "নেতিবাচক"},
    "gu": {"question_word": "ભાવના", "positive": "સકારાત્મક", "negative": "નકારાત્મક"},
    "hi": {"question_word": "भाव", "positive": "सकारात्मक", "negative": "नकारात्मक"},
    "kn": {"question_word": "ಭಾವನೆ", "positive": "ಸಕಾರಾತ್ಮಕ", "negative": "ನಕಾರಾತ್ಮಕ"},
    "ml": {"question_word": "വികാരം", "positive": "പോസിറ്റിവ്", "negative": "നെഗറ്റിവ്"},
    "mr": {"question_word": "भावना", "positive": "सकारात्मक", "negative": "नकारात्मक"},
    "or": {"question_word": "ଭାବନା", "positive": "ସକାରାତ୍ମକ", "negative": "ନକାରାତ୍ମକ"},
    "pa": {"question_word": "ਭਾਵਨਾ", "positive": "ਸਕਾਰਾਤਮਕ", "negative": "ਨਕਾਰਾਤਮਕ"},
    "ta": {"question_word": "உணர்வு", "positive": "நேர்மையானது", "negative": "எதிர்மையானது"},
    "te": {"question_word": "భావం", "positive": "అనుకూలం", "negative": "ప్రతికూలం"},
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


# doc_to_text_* functions
DOC_TO_TEXT = build_language_fns(doc_to_text)


# doc_to_choice_* functions
DOC_TO_CHOICE = build_language_fns(doc_to_choice)


for lang in LANGUAGES_WORDS:
    globals()[f"doc_to_text_{lang}"] = DOC_TO_TEXT[lang]
    globals()[f"doc_to_choice_{lang}"] = DOC_TO_CHOICE[lang]
