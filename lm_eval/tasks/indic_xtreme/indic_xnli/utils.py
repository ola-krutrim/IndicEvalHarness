from functools import partial
from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    string = f"Does the premise entail, contradict, or is neutral with respect to the hypothesis?\nAnswer 0 if premise entails the hypothesis, 1 if premise is neutral with respect to the hypothesis and 2 if it contradicts. Output the final answer as Answer: <Answer> where <Answer> is the final answer which is 0/1/2.\n\nPremise: {doc['premise']}\nHypothesis: {doc['hypothesis']}\nAnswer:"

    return string


def doc_to_choice(doc: Dict, connector: Dict[str, str]) -> list:
    """Convert a XNLI-style document into model choice text."""
    question_word = connector["question_word"].strip()
    entailment_label = connector["entailment_label"].strip()
    neutral_label = connector["neutral_label"].strip()
    contradiction_label = connector["contradiction_label"].strip()

    return [
        f"{doc['premise']}, {question_word}? {entailment_label}, {doc['hypothesis']}",
        f"{doc['premise']}, {question_word}? {neutral_label}, {doc['hypothesis']}",
        f"{doc['premise']}, {question_word}? {contradiction_label}, {doc['hypothesis']}",
    ]


# -------------------------
# Language words
# -------------------------
LANGUAGES_WORDS = {
    "as": {
        "question_word": "সঠিক",
        "entailment_label": "হʼয়",
        "neutral_label": "সঠিক? সেয়া হʼলে",
        "contradiction_label": "সঠিক? নহʼয়",
    },
    "bn": {
        "question_word": "সঠিক",
        "entailment_label": "হ্যাঁ",
        "neutral_label": "তাই",
        "contradiction_label": "না",
    },
    "gu": {
        "question_word": "સાચું",
        "entailment_label": "હા",
        "neutral_label": "તેથી",
        "contradiction_label": "નહીં",
    },
    "hi": {
        "question_word": "सही",
        "entailment_label": "हाँ",
        "neutral_label": "इसलिए",
        "contradiction_label": "नहीं",
    },
    "kn": {
        "question_word": "ಸರಿ",
        "entailment_label": "ಹೌದು",
        "neutral_label": "ಆದ್ದರಿಂದ",
        "contradiction_label": "ಇಲ್ಲ",
    },
    "ml": {
        "question_word": "ശരിയാണോ",
        "entailment_label": "ആണ്",
        "neutral_label": "അതിനാല്‍",
        "contradiction_label": "അല്ല",
    },
    "mr": {
        "question_word": "बरोबर",
        "entailment_label": "हो",
        "neutral_label": "म्हणून",
        "contradiction_label": "नाही",
    },
    "or": {
        "question_word": "ସଠିକ",
        "entailment_label": "ହଁ",
        "neutral_label": "ତେଣୁ",
        "contradiction_label": "ନାହିଁ",
    },
    "pa": {
        "question_word": "ਸਹੀ",
        "entailment_label": "ਹਾਂ",
        "neutral_label": "ਇਸ ਲਈ",
        "contradiction_label": "ਨਹੀਂ",
    },
    "ta": {
        "question_word": "சரியா",
        "entailment_label": "ஆம்",
        "neutral_label": "அதனால்",
        "contradiction_label": "இல்லை",
    },
    "te": {
        "question_word": "సరైనదా",
        "entailment_label": "అవును",
        "neutral_label": "అందుకే",
        "contradiction_label": "కాదు",
    },
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
