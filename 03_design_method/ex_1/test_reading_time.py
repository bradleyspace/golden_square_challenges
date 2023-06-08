from lib.reading_time import estimate_reading_time

def test_empty_string():
    assert estimate_reading_time("") == 0

def test_150_words():
    with open("texts/150words.txt", "r") as f:
        text = f.read()

    assert estimate_reading_time(text) == 1

# Given a text 200 words in length should return 1
# estimate_reading_time("<text with 200 words>") => 1

def test_200_words():
    with open("texts/200words.txt", 'r') as f:
        text = f.read()

    assert estimate_reading_time(text) == 1

# Given a text with 1000 words returns 5
# estimate_reading_time("<text with 1000 words") => 5

def test_1000_words():
    with open("texts/1000words.txt", "r") as f:
        text = f.read()

    assert estimate_reading_time(text) == 5

# Given a text with 1100 words returns 6
# estimate_reading_time("<text with 1100 words>") => 6

def test_1100_words():
    with open("texts/1100words.txt", "r") as f:
        text = f.read()

    assert estimate_reading_time(text) == 6

# Given a text from an article with 2637 - returns 13
# Included a integer in the text

def test_article():
    with open("texts/article.txt", "r") as f:
        text = f.read()

    assert estimate_reading_time(text) == 13
