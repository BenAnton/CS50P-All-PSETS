from seasons import get_birthdate

import pytest

def test_get_birthdate():
    with pytest.raises(SystemExit):
        get_birthdate("Hi")
    with pytest.raises(SystemExit):
        get_birthdate("11012001")
    with pytest.raises(SystemExit):
        get_birthdate("4th May 1987")

