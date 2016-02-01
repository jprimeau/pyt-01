from count_by import count_by

def test_list():
    assert str(type(count_by(1,10)))[1:-1] == "type 'list'"

def test_output():
    assert list(count_by(1, 5)) == [1, 2, 3, 4, 5]
    assert list(count_by(2, 5)) == [2, 4, 6, 8, 10]
    assert list(count_by(3, 5)) == [3, 6, 9, 12, 15]
    assert list(count_by(50, 5)) == [50, 100, 150, 200, 250]
    assert list(count_by(100, 5)) == [100, 200, 300, 400, 500]
    assert list(count_by(1, 1)) == [1]
    assert list(count_by(1, 10)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
