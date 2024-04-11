from um import count

def test_count():
    assert count('um') == 1
    assert count('Um') == 1
    assert count('UM') == 1
    assert count('um um UM Um') == 4
    assert count('um, um. UM! Um?') == 4
    assert count('ummm umm UMM Ummm') == 0
    assert count('dummy') == 0
    assert count('') == 0

