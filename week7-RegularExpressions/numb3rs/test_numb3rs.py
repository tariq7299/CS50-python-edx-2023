import pytest
from numb3rs import validate

def test_format_of_ip():
    assert validate("255.1.2") == False
    assert validate("233.2.23.113") == True
    assert validate("199.0") == False
    assert validate("34") == False

def test_range_of_ip():
    assert validate("256.1.2.13") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("255.255.255.255.255") == False
    assert validate("-1.0.0.0") == False
