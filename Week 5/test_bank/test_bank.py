from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("goodbye") == 100

def test_caps():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("Goodbye") == 100

def test_spaces():
    assert value(" hello") == 0
    assert value("hello ") == 0
