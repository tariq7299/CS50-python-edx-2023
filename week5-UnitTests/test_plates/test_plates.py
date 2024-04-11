from plates import is_valid



def test_false_plates():
    assert is_valid("50CS") == False
    assert is_valid("CS50HELLO") == False
    assert is_valid("CS5$") == False
    assert is_valid("C") == False
    assert is_valid("CS05") == False
    assert is_valid("CS57f") == False
    assert is_valid("4DSD") == False

def test_plates_without_checks_for_zero_placement():
    assert is_valid("#$C5") == False
    assert is_valid("#$C5") == False
    assert is_valid("#$C5") == False

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELL") == True
    assert is_valid("TA403") == True

