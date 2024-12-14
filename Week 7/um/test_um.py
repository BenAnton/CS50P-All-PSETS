from um import count

def test_count():
    assert count("um") == 1
    assert count("um um um um") == 4


def test_no_find():
    assert count("Hello") == 0
    assert count("number album strum") == 0

def test_punct():
    assert count("um, um. um? um!") == 4

def test_case():
    assert count("UM UM UM UM") == 4
