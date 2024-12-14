from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_error():
    with pytest.raises(ValueError):
        convert("Hello")

def test_error2():
    with pytest.raises(ValueError):
        convert("25 AM to 5 PM")

def test_error3():
    with pytest.raises(ValueError):
        convert("9 5")

def test_error4():
    with pytest.raises(ValueError):
        convert("9am 5pm")

def test_error5():
    with pytest.raises(ValueError):
        convert("9:70 to 10:00")

def test_error6():
    with pytest.raises(ValueError):
        convert("9am to 5:000")

def test_error7():
    with pytest.raises(ValueError):
        convert(" 9:00am - 5:00pm")

def test_error8():
    with pytest.raises(ValueError):
        convert(" 9:00am - 5:00pm ")

def test_error9():
    with pytest.raises(ValueError):
        convert("29:00am - 5:00pm")

def test_error10():
    with pytest.raises(ValueError):
        convert("9:00am - 25:00pm")

