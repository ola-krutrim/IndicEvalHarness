from typing import Dict


LANGS = ["bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    prompt = f"{doc['passage']}\n\n{doc['question']}\nyes/no?"

    return prompt


def doc_to_choice(doc: Dict) -> list:
    return ["no", "yes"]
