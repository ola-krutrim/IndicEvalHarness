from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    choices = doc["choices"]["text"]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = "Question: " + doc["question"] + "\nChoices:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Answer:"

    return prompt


def doc_to_choice(doc: Dict) -> list:
    return doc["choices"]["text"]


def doc_to_target(doc: Dict) -> list:
    return doc["choices"]["label"].index(doc["answerKey"])
