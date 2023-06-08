from lib.reading_time import estimate_reading_time

def test_empty_string():
    assert estimate_reading_time("") == 0

def test_150_words():
    with open("texts/150words.txt", "r") as f:
        text = f.read()

    assert estimate_reading_time(text) == 1



