from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    question = doc["question"].strip()
    choices = []
    for i in range(4):
        choices.append(convert_choice(doc[f"option{i + 1}"]).strip())

    prompt = f"Question:{question}\nChoices:\nA:{choices[0]},\nB:{choices[1]},\nC:{choices[2]},\nD:{choices[3]}\nAnswer:"

    return prompt.rstrip()


def doc_to_choice(doc: Dict) -> list:
    return ["A", "B", "C", "D"]


def doc_to_target(doc: Dict) -> list:
    target_map = {"option1": "A", "option2": "B", "option3": "C", "option4": "D"}

    return target_map[doc["target"]]


def convert_choice(choice):
    return choice[0].lower() + choice[1:]
