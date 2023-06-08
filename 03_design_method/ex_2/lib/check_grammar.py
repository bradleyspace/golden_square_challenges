import string

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

    punctuation = ["!", "?", "."]

    if len(text) <= 0:
        return None

    if text[-1] not in punctuation:
        return False
    
    if text[0] not in string.ascii_uppercase:
        return False

    return True