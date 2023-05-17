import pytest


def prime(n):
    lst = []
    divider = 2
    while n > 1:
        while n % divider == 0:
            lst.append(divider)
            n /= divider
        divider += 1
    return lst


@pytest.mark.parametrize('number, result',
                         [
                             (1, []),
                             (2, [2]),
                             (3, [3]),
                             (4, [2, 2]),
                             (5, [5]),
                             (6, [2, 3]),
                             (7, [7]),
                             (8, [2, 2, 2]),
                             (9, [3, 3]),
                         ])
def test_prime(number, result):
    assert prime(number) == result
