import pytest
from working import convert

# Unit tests
def test_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12:00 am to 1:00 pm') == '00:00 to 13:00'
    assert convert('1:00 pm to 2:00 pm') == '13:00 to 14:00'
    assert convert('12:00 pm to 1:00 am') == '12:00 to 01:00'
    assert convert('11:59 pm to 12:01 am') == '23:59 to 00:01'
    assert convert('12 am to 1 pm') == '00:00 to 13:00'
    assert convert('1 pm to 2 pm') == '13:00 to 14:00'
    assert convert('12 pm to 1 am') == '12:00 to 01:00'
    assert convert('11 pm to 12 am') == '23:00 to 00:00'

    with pytest.raises(ValueError):
        convert('13 PM to 17 PM')
    with pytest.raises(ValueError):
        convert('13:70 am to 1:67 pm')
    with pytest.raises(ValueError):
        convert('12:00 am to 13:00 pm')
    with pytest.raises(ValueError):
        convert('12:60 am to 1:00 pm')
    with pytest.raises(ValueError):
        convert('12:00 am to 1:60 pm')
    with pytest.raises(ValueError):
        convert('12:00 xm to 1:00 pm')
    with pytest.raises(ValueError):
        convert('12:00 am to 1:00 xm')
    with pytest.raises(ValueError):
        convert('12 to 1 pm')
    with pytest.raises(ValueError):
        convert('12 pm to 1')
    with pytest.raises(ValueError):
        convert('12 pm - 1')
    with pytest.raises(ValueError):
        convert('invalid input')

if __name__ == "__main__":
    pytest.main()
