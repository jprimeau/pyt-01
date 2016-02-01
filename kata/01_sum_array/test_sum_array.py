from sum_array import sum_array

def test_int():
    assert str(type(sum_array([1,2])))[1:-1] == "type 'int'"

def test_float():
    assert str(type(sum_array([1.1,2])))[1:-1] == "type 'float'"

def test_output():
    assert sum_array([]) == 0
    assert sum_array([1]) == 1
    assert sum_array([1,2]) == 3
    assert sum_array([1,10,100]) == 111
    assert sum_array([1.1,2.2,3.3]) == 6.6
