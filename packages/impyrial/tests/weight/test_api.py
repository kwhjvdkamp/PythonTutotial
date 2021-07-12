from impyrial.weight.api import (
    convert_unit
)

from impyrial.weight.core import (
    UNITS,
    ounces_to_pounds,
    ounces_to_stone,
)

# UNITS = ("oz", "lb", "st")

def test_weight_convert_unit():

    assert convert_unit(1, UNITS[0], UNITS[0]) == 1
    assert convert_unit(1, UNITS[0], UNITS[0]) != 1.01
    assert convert_unit(1, UNITS[1], UNITS[1]) == 1
    assert convert_unit(1, UNITS[1], UNITS[1]) != 1.01
    assert convert_unit(1, UNITS[2], UNITS[2]) == 1
    assert convert_unit(1, UNITS[2], UNITS[2]) != 1.01

    assert convert_unit(1, UNITS[0], UNITS[1]) == ounces_to_pounds(1)
    assert convert_unit(1, UNITS[0], UNITS[2]) == ounces_to_stone(1)

    assert convert_unit(1, UNITS[0], UNITS[1]) != ounces_to_pounds(1.01)
    assert convert_unit(1, UNITS[0], UNITS[2]) != ounces_to_stone(1.01)

    # Reverse=True
    assert convert_unit(1, UNITS[1], UNITS[0]) == ounces_to_pounds(1, reverse=True)
    assert convert_unit(1, UNITS[2], UNITS[0]) == ounces_to_stone(1, reverse=True)

    assert convert_unit(1,UNITS[1],UNITS[0]) != ounces_to_pounds(1.01, reverse=True)
    assert convert_unit(1,UNITS[2],UNITS[0]) != ounces_to_stone(1.01, reverse=True)