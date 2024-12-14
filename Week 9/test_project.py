import pytest
from project import convert_what, convert_length, convert_weight, convert_area, convert_time, convert_temperature

def test_convert_what():
    with pytest.raises(ValueError):
        convert_what("Hello")

def test_convert_length():
    assert convert_length("cm", "m", 100) == 1

def test_convert_weight():
    assert convert_weight("kg", "lbs", 1) == 2.205

def test_convert_area():
    assert convert_area("miles", "acres", 1) == 640

def test_convert_time():
    assert convert_time("seconds", "minutes", 60) == 1

def test_convert_temperature():
    assert convert_temperature("c", "f", 1) == 33.8

