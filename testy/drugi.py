def sqrt(x):
    assert x >= 0
    precision = 0.0001
    step = 1
    start = 0
    while abs(start * start - x) > precision:
        start += step
        if start * start > x:
            start -= step
            step /= 10
    return start


def test_check():
    try:
        sqrt(-1)
        assert False
    except Exception:
        assert True


def test_001():
    assert sqrt(16) == 4


def test_002():
    assert sqrt(4) == 2


def test_003():
    assert sqrt(64) == 8


def test_004():
    assert sqrt(25) == 5


def test_005():
    assert sqrt(20) != 4
