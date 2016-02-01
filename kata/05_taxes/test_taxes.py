from taxes import taxes

def test_dict():
    assert str(type(taxes(1.00)))[1:-1] == "type 'dict'"

def test_length():
    assert len(taxes(1.00)) == 4

def test_keys():
    assert 'amount' in taxes(1.00)
    assert 'gst' in taxes(1.00)
    assert 'qst' in taxes(1.00)
    assert 'total' in taxes(1.00)

def test_output():
    r = taxes(1.00)
    assert str(r['amount']) == '1.00$'
    assert str(r['gst']) == '0.05$'
    assert str(r['qst']) == '0.10$'
    assert str(r['total']) == '1.15$'

    r = taxes(1.05)
    assert str(r['amount']) == '1.05$'
    assert str(r['gst']) == '0.05$'
    assert str(r['qst']) == '0.10$'
    assert str(r['total']) == '1.20$'

    r = taxes(1.06)
    assert str(r['amount']) == '1.06$'
    assert str(r['gst']) == '0.05$'
    assert str(r['qst']) == '0.11$'
    assert str(r['total']) == '1.22$'
    
    r = taxes(10.38)
    assert str(r['amount']) == '10.38$'
    assert str(r['gst']) == '0.52$'
    assert str(r['qst']) == '1.04$'
    assert str(r['total']) == '11.94$'
    
    r = taxes(112.12)
    assert str(r['amount']) == '112.12$'
    assert str(r['gst']) == '5.61$'
    assert str(r['qst']) == '11.18$'
    assert str(r['total']) == '128.91$'
