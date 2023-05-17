def add(a, b):
    return a + b


def test_001():
    assert add(1, 1) == 2


def test_002():
    assert add(1, 2) == 3


def test_003():
    assert add(0, 1) == 1


def test_004():
    assert add(1, -1) == 0


def test_005():
    assert add(100, 200) == 300


def test_006():
    assert add(0, -10) == -10


def test_007():
    assert add(12, 4) == 16
