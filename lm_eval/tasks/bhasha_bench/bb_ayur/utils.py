from typing import Dict


# -------------------------
# Core utilities
# -------------------------
def doc_to_text(doc: Dict) -> str:
    """
    To create a prompt for generation based task evaluation
    """
    choices = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
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
    return [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]


def doc_to_target(doc: Dict) -> list:
    """
    Returns the index of the correct answer in the list of choices
    """
    answer_text = doc["correct_answer"]
    options = ["A", "B", "C", "D"]
    option_key = options.index(answer_text)

    return option_key
