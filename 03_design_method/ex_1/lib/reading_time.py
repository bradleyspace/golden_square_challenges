def estimate_reading_time(text: str) -> int:
    """
    Parameters:
        text: A string containing the text to be read

    Returns:
        int: Representing the number of minutes

    Side-Effects:
        Could return 0 if the text was an empty string
    """
    
    if len(text) == 0:
        return 0
    num_words = len(text.split(" "))
    average_wpm = 200
    reading_time = num_words / average_wpm
    if reading_time < 1:
        return 1
    
    return round(reading_time)