from leapyear import leap

def test_year_2012():
    assert leap(2012) == "leap year"

def test_year_2023():
    assert leap(2023) == "not leap year"

def test_year_2000():
    assert leap(2000) == "leap year"

def test_year_1900():
    assert leap(1900) == "not leap year"
