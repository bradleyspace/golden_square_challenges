from lib.check_grammar import check_grammar

# # Pass a text that is gramatically correct, return True
# check_grammar("Hello there.") => True

def test_correct_grammar():
    text = "I like food!"
    assert check_grammar(text) == True

# # Pass a text that has a captial letter but no end of sentance punctation, return False
# check_grammar("Hello Rich") => False

def test_no_punctuation():
    text = "Hello Rich"
    assert check_grammar(text) == False

# # Pass a text that doesn't have a captial letter but does have end of sentance punctuation, return True
# check_grammar("hello Rich.") => False

def test_no_captial():
    text = "hello Rich."
    assert check_grammar(text) == False

# # Pass a empty string which should return None
# check_grammar("") => None

def test_empty_string():
    assert check_grammar("") == None