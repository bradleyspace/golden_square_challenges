## Function

```python
def check_if_todo(text: str) -> bool:
    """
    Parameters:
        text: A string containing the text to check
    Returns:
        bool: Whether the text has '#TODO' 
    Side Effects:
        None
    """
    pass
```

## Tests

```python

# Given an empty string
check_if_todo("") => False

# Given a string that contains '#TODO'
check_if_todo("#TODO: Write the function!") => True

# Given a string that contains '#todo' ( lowercase )
check_if_todo("#todo: Write the function!") => True

# Given a string that doesn't contain '#TODO'
check_if_todo("Write the function!") => False

# Given a string that contains 'TODO' (No #)
check_if_todo("TODO: Write the function!") => False

# Given a string that contains '#'
check_if_todo("# Write the function!") => False
```