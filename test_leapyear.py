from leapyear import leap


def test_leap_year():
    assert leap(2024) == True


def test_not_leap_year():
    assert leap(2023) == False


def test_century_not_leap_year():
    assert leap(1900) == False


def test_century_leap_year():
    assert leap(2000) == True