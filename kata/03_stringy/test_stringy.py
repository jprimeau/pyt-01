from stringy import stringy

def test_string():
    assert str(type(stringy(5)))[1:-1] == "type 'str'"

def test_start_with_1():
    assert stringy(10)[0] == '1'

def test_length():
    for i in xrange(1, 5):
        assert len(stringy(i)) == i

def test_output():
    assert stringy(1) == '1'
    assert stringy(2) == '10'
    assert stringy(5) == '10101'
    assert stringy(10) == '1010101010'
    assert stringy(13) == '1010101010101'
