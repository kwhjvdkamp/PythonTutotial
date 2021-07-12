from impyrial.length.api import (
    convert_unit
)

from impyrial.length.core import (
    UNITS,
    inches_to_feet,
    inches_to_yards,
)

# UNITS = ("in", "ft", "yd")

def test_length_convert_unit():

    assert convert_unit(1,UNITS[0],UNITS[0]) == 1
    assert convert_unit(1,UNITS[0],UNITS[0]) != 1.01
    assert convert_unit(1,UNITS[1],UNITS[1]) == 1
    assert convert_unit(1,UNITS[1],UNITS[1]) != 1.01
    assert convert_unit(1,UNITS[2],UNITS[2]) == 1
    assert convert_unit(1,UNITS[2],UNITS[2]) != 1.01

    assert convert_unit(1,UNITS[0],UNITS[1]) == inches_to_feet(1)
    assert convert_unit(1,UNITS[0],UNITS[2]) == inches_to_yards(1)

    assert convert_unit(1,UNITS[0],UNITS[1]) != inches_to_feet(1.01)
    assert convert_unit(1,UNITS[0],UNITS[2]) != inches_to_yards(1.01)

    # Reverse=True
    assert convert_unit(1,UNITS[1],UNITS[0]) == inches_to_feet(1, reverse=True)
    assert convert_unit(1,UNITS[2],UNITS[0]) == inches_to_yards(1, reverse=True)

    assert convert_unit(1,UNITS[1],UNITS[0]) != inches_to_feet(1.01, reverse=True)
    assert convert_unit(1,UNITS[2],UNITS[0]) != inches_to_yards(1.01, reverse=True)
