from impyrial.utils import (
    check_units
)

def test_check_units():
    assert check_units('oz', 'oz', ("oz", "lb", "st"))
