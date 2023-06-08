## Goal

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

```python
def estimate_reading_time(text: str) -> int:
    """
    Parameters:
        text: A string containing the text to be read

    Returns:
        int: Representing the number of minutes

    Side-Effects:
        Could return 0 if the text was an empty string
    """
```

```python

# Given an empty string, return 0
estimate_reading_time("") => 0

# Given text less than 200 words, return float to 1.dp
# For example: text with 150 words should return 0.75, so
# output should be 0.8
estimate_reading_time("<text with 150 words>") => 1

# Given a text 200 words in length should return 1
estimate_reading_time("<text with 200 words>") => 1

# Given a text with 1000 words returns 5
estimate_reading_time("<text with 1000 words") => 5

# Given a text with 1100 words returns 6
estimate_reading_time("<text with 1100 words>") => 6
```
