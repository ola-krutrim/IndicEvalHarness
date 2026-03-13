from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    choices = []
    for i in range(4):
        choices.append(convert_choice(doc["choices"][i]))
    prompt = f"Question: {doc['question']}\nChoices:\nA:{choices[0]}\nB:{choices[1]}\nC:{choices[2]}\nD:{choices[3]}\nAnswer:"

    return prompt


def doc_to_choice(doc: Dict) -> list:
    return ["A", "B", "C", "D"]


def doc_to_target(doc: Dict) -> list:
    target_map = ["A", "B", "C", "D"]

    return target_map[doc["answer"]]


def convert_choice(choice):
    """
    Convert the first character of a choice string to lowercase, preserving the rest.
    """
    return choice[0].lower() + choice[1:]
