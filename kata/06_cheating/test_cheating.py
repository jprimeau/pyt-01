import calendar
import time

from cheating import removeNb

def test_output():
    assert removeNb(100) == []
    assert removeNb(26) == [(15, 21), (21, 15)]
    assert removeNb(32) == []
    assert removeNb(906) == [(505, 811), (615, 666), (637, 643), (643, 637), (666, 615), (811, 505)]
    assert removeNb(990) == [(517, 946), (946, 517)]
    assert removeNb(2720) == [(1548, 2388), (2388, 1548)]
    assert removeNb(10000) == []

def test_performance():
    start = calendar.timegm(time.gmtime())
    removeNb(15000)
    assert calendar.timegm(time.gmtime()) - start < 6
