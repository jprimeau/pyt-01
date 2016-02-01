from vowel_remover import shortcut

def test_string():
    assert str(type(shortcut('test')))[1:-1] == "type 'str'"

def test_output():
    assert shortcut('alpha') == 'lph'
    assert shortcut('echo') == 'ch'
    assert shortcut('india') == 'nd'
    assert shortcut('oscar') == 'scr'
    assert shortcut('uniform') == 'nfrm'
    assert shortcut('yanki') == 'nk'
    assert shortcut('aeiouy') == ''
    assert shortcut('aaa') == ''
    assert shortcut('hello, how are you?') == 'hll, hw r ?'
    assert shortcut('AEIOUY') == 'AEIOUY'
