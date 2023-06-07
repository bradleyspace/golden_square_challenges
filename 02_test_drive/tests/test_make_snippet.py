from lib.make_snippet import make_snippet

def test_make_snippet():
    assert make_snippet("The weather is very nice today!") == "The weather is very nice..."
    assert make_snippet("Hello World!") == "Hello World!"