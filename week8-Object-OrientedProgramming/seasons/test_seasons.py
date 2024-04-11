from seasons import convert


def test_date():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(5735520) == "Eight billion, two hundred fifty-nine million, one hundred forty-eight thousand, eight hundred minutes"
