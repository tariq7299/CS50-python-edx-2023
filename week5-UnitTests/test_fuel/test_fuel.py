import pytest
from fuel import gauge, convert

def test_convert():
    assert convert("3/4") == 75

    with pytest.raises(ValueError):
        convert("s/f")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()
