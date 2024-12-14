import pytest
from twttr import shorten


def test_upper():
    assert shorten("BEN") == ("BN")

def test_lower():
    assert shorten("ben") == ("bn")

def test_spaces():
    assert shorten("Ben Ben") == ("Bn Bn")

def test_punc():
    assert shorten("Ben!") == ("Bn!")

def test_blank():
    assert shorten(" ") == (" ")

def test_num():
    assert shorten("Ben1") == ("Bn1")
