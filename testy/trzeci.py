from datetime import datetime

import pytest


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 != 0 else "female"
    # if 81 <= int(pesel[2:4]) <= 92:
    #     birth_date = datetime(int("18" + pesel[0: 2]), int(pesel[2:4]) - 80, int(pesel[4:6]))
    # elif 1 <= int(pesel[2:4]) <= 12:
    #     birth_date = datetime(int("19" + pesel[0: 2]), int(pesel[2:4]), int(pesel[4:6]))
    # elif 21 <= int(pesel[2:4]) <= 32:
    #     birth_date = datetime(int("20" + pesel[0: 2]), int(pesel[2:4]) - 20, int(pesel[4:6]))
    # elif 41 <= int(pesel[2:4]) <= 52:
    #     birth_date = datetime(int("21" + pesel[0: 2]), int(pesel[2:4]) - 40, int(pesel[4:6]))
    # elif 61 <= int(pesel[2:4]) <= 72:
    #     birth_date = datetime(int("22" + pesel[0: 2]), int(pesel[2:4]) - 60, int(pesel[4:6]))
    # else:
    #     raise ValueError
    month = int(pesel[2:4])
    years = {
        0: '19',
        1: '20',
        2: '21',
        3: '22',
        4: '18'
    }
    year = int(years[month // 20] + pesel[0: 2])
    month = month % 20
    birth_date = datetime(year, month, int(pesel[4:6]))

    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


@pytest.mark.parametrize('pesel, expected',
                         [
                             ('98050276973', True),
                             ('79022635965', True),
                             ('98051276973', False)
                         ])
def test_is_valid(pesel, expected):
    result = analyze_pesel(pesel)
    assert result['valid'] == expected


def test_if_pesel_field_ok():
    pesel = '98052454775'
    result = analyze_pesel(pesel)
    assert result.get('pesel') == pesel


def test_if_gender_male_01():
    pesel = '98052454775'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'male'


def test_if_gender_male_02():
    pesel = '62071763257'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'male'


def test_if_gender_male_03():
    pesel = '82101996998'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'male'


def test_if_gender_male_04():
    pesel = '97090399457'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'male'


def test_if_gender_female_01():
    pesel = '98052454725'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'female'


def test_if_gender_female_02():
    pesel = '79022635965'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'female'


def test_if_gender_female_03():
    pesel = '06312342265'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'female'


def test_if_gender_female_04():
    pesel = '84060256544'
    result = analyze_pesel(pesel)
    assert result.get('gender') == 'female'


def test_if_pesel_is_valid_01():
    pesel = '98050276973'
    result = analyze_pesel(pesel)
    assert result.get('valid')


def test_if_pesel_is_valid_02():
    pesel = '79022635965'
    result = analyze_pesel(pesel)
    assert result.get('valid')


def test_if_pesel_is_not_valid():
    pesel = '98051276973'
    result = analyze_pesel(pesel)
    # assert result.get('valid') is False
    assert not result.get('valid')


def test_birth_day_1800():
    pesel = '98850276973'
    result = analyze_pesel(pesel)
    assert result.get('birth_date') == datetime(1898, 5, 2)


def test_birth_day_1900():
    pesel = '98050276973'
    result = analyze_pesel(pesel)
    assert result.get('birth_date') == datetime(1998, 5, 2)


def test_birth_day_2000():
    pesel = '98250276973'
    result = analyze_pesel(pesel)
    assert result.get('birth_date') == datetime(2098, 5, 2)


def test_birth_day_2100():
    pesel = '98450276973'
    result = analyze_pesel(pesel)
    assert result.get('birth_date') == datetime(2198, 5, 2)


def test_birth_day_2200():
    pesel = '98650276973'
    result = analyze_pesel(pesel)
    assert result.get('birth_date') == datetime(2298, 5, 2)
