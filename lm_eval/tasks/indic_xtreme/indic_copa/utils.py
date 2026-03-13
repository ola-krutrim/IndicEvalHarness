from functools import partial
from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def convert_choice(choice: str) -> str:
    """Lowercase the first character of a choice string."""
    return choice[0].lower() + choice[1:]


def doc_to_text(doc: Dict, connector: Dict[str, str]) -> str:
    """Convert a COPA-style document into model input text."""
    conn = connector[doc["question"]].strip()
    return (
        f"{doc['premise'].strip()[:-1]}\n"
        f"{conn}\n"
        f"A: {convert_choice(doc['choice1'])}\n"
        f"B: {convert_choice(doc['choice2']).strip()}\n"
        f"Answer:"
    )


def doc_to_choice(doc: Dict):
    return ["A", "B"]


def doc_to_target(doc: Dict) -> str:
    """Map dataset label to choice."""
    return {"0": "A", "1": "B"}.get(str(doc["label"]).strip())


# -------------------------
# Language connectors
# -------------------------
CAUSE_EFFECT_CONNECTORS = {
    "as": {"cause": "কাৰণত", "effect": "তেতিয়া"},
    "bn": {"cause": "কারণ", "effect": "সুতরাং"},
    "en": {"cause": "because", "effect": "therefore"},
    "gu": {"cause": "કારણે", "effect": "તેથી"},
    "hi": {"cause": "क्योंकि", "effect": "इसलिए"},
    "kn": {"cause": "ಏಕೆಂದರೆ", "effect": "ಆದುದರಿಂದ"},
    "ml": {"cause": "കാരണം", "effect": "അതുകൊണ്ട്"},
    "mr": {"cause": "कारण", "effect": "म्हणून"},
    "pa": {"cause": "ਕਿਉਂਕਿ", "effect": "ਇਸ ਲਈ"},
    "or": {"cause": "କାରଣ", "effect": "ଏହିକାରଣରୁ"},
    "ta": {"cause": "காரணமாக", "effect": "எனவே"},
    "te": {"cause": "కారణంగా", "effect": "కాబట్టి"},
    "ur": {"cause": "کیونکہ", "effect": "لہٰذا"},
}


# -------------------------
# Language-specific adapters
# -------------------------
def build_language_fns(base_fn):
    """
    Generate language-specific partial functions for doc_to_text / copa_text.
    """
    return {
        lang: partial(base_fn, connector=connector)
        for lang, connector in CAUSE_EFFECT_CONNECTORS.items()
    }


# doc_to_text_* functions
DOC_TO_TEXT = build_language_fns(doc_to_text)


for lang in CAUSE_EFFECT_CONNECTORS:
    globals()[f"doc_to_text_{lang}"] = DOC_TO_TEXT[lang]
