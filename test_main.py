import pytest

from main import evaluate


def test_foo():
    assert True


def test_correct_place():
    assert evaluate(
        ["blue", "red", "green", "pink"], ["brown", "red", "white", "yellow"]
    ) == [1, 0]


def test_wrong_length():
    with pytest.raises(ValueError):
        evaluate(["blue", "red"], ["red", "red"])


def test_misplaced():
    assert evaluate(
        ["blue", "red", "green", "pink"], ["red", "yellow", "brown", "white"]
    ) == [0, 1]


def test_correct_and_misplaced():
    assert evaluate(
        ["blue", "red", "green", "pink"], ["yellow", "red", "blue", "purple"]
    ) == [1, 1]


def test_no_repeats():
    with pytest.raises(ValueError):
        evaluate(
            ["blue", "red", "green", "pink"], ["red", "red", "blue", "purple"]
        )


def test_correct_guess():
    assert evaluate(
        ["blue", "red", "green", "pink"], ["blue", "red", "green", "pink"]
    ) == [4, 0]


def test_invalid_color():
    with pytest.raises(ValueError):
        evaluate(
            ["blue", "red", "green", "pink"], ["blurple", "red", "blue", "purple"]
        )
