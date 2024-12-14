# from plates import min_max, starts_with_letters, ends_with_numbers, punctuation_check
from plates import is_valid

def test_min_max():
    assert is_valid("D") == False
    assert is_valid("DDDDDDD") == False
    assert is_valid("DDDD") == True

def test_starts_with_letters():
    assert is_valid("AAAA") == True
    assert is_valid("A1AA") == False
    assert is_valid("1AAA") == False
    assert is_valid("11") == False
    assert is_valid("AA") == True

def test_ends_with_numbers():
    assert is_valid("DDD1") == True
    assert is_valid("SS123") == True
    assert is_valid("0DDD") == False
    assert is_valid("DDD0") == False
    assert is_valid("11DD") == False
    assert is_valid("00") == False
    assert is_valid("WW00") == False
    assert is_valid("WW11WW") == False



def test_punctuation_check():
    assert is_valid("!SDSF") == False
    assert is_valid("SFG?X") == False
