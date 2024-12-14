from numb3rs import validate


def test_validate_ip():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_length():
    assert validate("1.1.1.1.1") == False
    assert validate("1.1") == False

def test_byte():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.500.500.500") == False

