from lib.check_if_todo import check_if_todo

# # Given an empty string
# check_if_todo("") => False

def test_empty_string():
    assert check_if_todo("") is False


# # Given a string that contains '#TODO'
# check_if_todo("#TODO: Write the function!") => True

def test_contains_todo():
    text = "#TODO: Write the function!"
    assert check_if_todo(text) is True

# # Given a string that contains '#todo' ( lowercase )
# check_if_todo("#todo: Write the function!") => True

def test_lowercase_todo():
    text = "#todo: Write the function!"
    assert check_if_todo(text) is True

# # Given a string that doesn't contain '#TODO'
# check_if_todo("Write the function!") => False

def test_no_todo():
    text = "Write the function!"
    assert check_if_todo(text) is False

# # Given a string that contains 'TODO' (No #)
# check_if_todo("TODO: Write the function!") => False

def test_no_hash():
    text = "TODO: Write the function!"
    assert check_if_todo(text) is False

# # Given a string that contains '#'
# check_if_todo("# Write the function!") => False

def test_single_hash():
    text = "# Write the function!"
    assert check_if_todo(text) is False

