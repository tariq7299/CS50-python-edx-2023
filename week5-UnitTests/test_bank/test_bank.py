from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO !!") == 0

def test_h():
    assert value("hekoo") == 20
    assert value("Hareboo") == 20

def test_else():
    assert value("Mark") == 100
