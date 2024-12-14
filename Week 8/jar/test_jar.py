from jar import Jar
import pytest

@pytest.fixture
def jar():
    capacity = 12
    return Jar(capacity = capacity)

def test_initial(jar):
    assert jar.size == 0

def test_deposit(jar):
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw(jar):
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

def test_capacity(jar):
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_negative_cookies(jar):
    with pytest.raises(ValueError):
        jar.withdraw(1)
