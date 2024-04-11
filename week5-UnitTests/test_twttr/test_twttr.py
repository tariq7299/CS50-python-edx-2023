from twttr import shorten

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_no_vowels():
    assert shorten("xyz") == "xyz"

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""

def test_shorten_mixed_text():
    assert shorten("Hello World") == "Hll Wrld"

def test_shorten_text_with_numbers():
    assert shorten("Hello Worl332d 2233") == "Hll Wrl332d 2233"

def test_shorten_text_with_capital_letters():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_shorten_with_puncituation():
    assert shorten("Hello, World!!?") == "Hll, Wrld!!?"
