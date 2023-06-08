from lib.exercise1 import DiaryEntry

TITLE = "My Diary"

with open("text/long_diary_entry.txt", "r") as f:
    FILE_CONTENTS = f.read()
    diary = DiaryEntry(title=TITLE, contents=FILE_CONTENTS)

# Title: "My Diary"
# Content: "This is my Diary:

# Check the function formats correctly
# DiaryEntry.format() => "My Dairy: This is my Diary"

def test_format():
    result = diary.format()

    assert result == f"{TITLE}: {FILE_CONTENTS}"

# # Count words returns the number of words in the diary entry
# DiaryEntry.count_words() => 4

def test_count_words():
    result = diary.count_words()
    assert result == 491

# # Check the reading time for specified wpm
# DiaryEntry.reading_time(1) => 4

def test_reading_time():
    result = diary.reading_time(100)
    assert result == 5

# # These tests below need to be completed with the same class instance

def test_reading_chunk():
    wpm = 100
    minutes = 2
    words = FILE_CONTENTS.split(" ")
    chunk = diary.reading_chunk(wpm, minutes)

    expected_chunk_1 = " ".join(words[0:200])
    assert chunk == expected_chunk_1

    chunk = diary.reading_chunk(wpm, minutes)
    expected_chunk_2 = " ".join(words[200:400])

    assert chunk == expected_chunk_2
    print("passed chunk 2!")

    chunk = diary.reading_chunk(wpm, minutes)
    expected_chunk_3 = " ".join(words[400:491])

    assert chunk == expected_chunk_3


    chunk = diary.reading_chunk(wpm, minutes)
    
    assert chunk == expected_chunk_1

# # Title: "My Diary"
# # Content: "text/long_diary_entry.txt"

# # Check the correct length reading chunk is returned.
# # 100 wpm for 2 minutes returns a string of length 200
# DiaryEntry.reading_chunck(100, 2) => "<String with 200 words>"

# # Check that the chunck of words starts from the next possible word
# # 100 wpm for 2 minutues returns the next 200 words
# DiaryEntry.reading_chunck(100, 2) => "<next available 200 words>"

# # Check that the chunck of words returned at the end of the text is 150
# # if 150 words are left and reading chunck is over 150 words
# DiaryEntry.reading_chunck(100, 2) => "<last 150 words>"

# # Check that the chunck of words returned after returning all the text
# # is the first section of the diary entry
# DiaryEntry.reading_chunck(100, 2) => "<first 200 words>"

