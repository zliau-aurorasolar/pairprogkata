from typing import List


valid_colours = [
    "purple",
    "pink",
    "red",
    "blue",
    "yellow",
    "green",
    "white",
    "brown",
]


def evaluate(code: List[str], guess: List[str]) -> List[int]:
    global valid_colours

    if len(code) != 4 or len(guess) != 4:
        raise ValueError

    if (
        not set(code).issubset(set(valid_colours))
        or not set(guess).issubset(set(valid_colours))
    ):
        raise ValueError("Unexpected colour")

    if len(code) != len(set(code)) or len(guess) != len(set(guess)):
        raise ValueError

    correct_place: int = 0
    correct_colour: int = 0

    for index, guess_item in enumerate(guess):
        if guess_item == code[index]:
            correct_place += 1
        elif guess_item in code:
            correct_colour += 1

    return [correct_place, correct_colour]
