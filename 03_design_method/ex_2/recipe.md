## Function

```python

def check_grammar(text: str) -> bool:
    """
    Parameters: 
        text: string containing the grammar to be checked
    
    Return:
        boolean: represents whether it started with a captial
                and ended with a full stop, or not.
    
    Side effects:
        Empty string -> return None
        Text starts with number (e.g. 10) -> return False
    """
```

## Tests

```python

# Pass a text that is gramatically correct, return True
check_grammar("Hello there.") => True

# Pass a text that has a captial letter but no end of sentance punctation, return False
check_grammar("Hello Rich") => False

# Pass a text that doesn't have a captial letter but does have end of sentance punctuation, return True
check_grammar("hello Rich.") => False

# Pass a empty string which should return None
check_grammar("") => None

```