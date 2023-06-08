def check_if_todo(text: str) -> bool:
    """
    Parameters:
        text: A string containing the text to check
    Returns:
        bool: Whether the text has '#TODO' 
    Side Effects:
        None
    """
    
    string_to_search = "#TODO"

    if string_to_search in text.upper():
        return True
    
    return False