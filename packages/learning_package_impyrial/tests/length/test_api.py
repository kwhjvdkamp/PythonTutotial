from length.api import (
    convert_unit
)

from packaging_according_impyrial.learning_package_impyrial.length.core import (
    UNITS,
    inches_to_feet,
    inches_to_yards,
)

def test_convert_unit(x, from_unit, to_unit):

    assert convert_unit(1,'in','in') == 1
    assert convert_unit(1,'in','in') != 1.01

    assert convert_unit(1,'in','ft') == inches_to_feet(1)
    assert convert_unit(1,'in','yd') == inches_to_yards(1)

    assert convert_unit(1,'in','ft') != inches_to_feet(1.01)
    assert convert_unit(1,'in','yd') != inches_to_yards(1.01)

    # Reverse=True
    assert convert_unit(1,'ft','in') == inches_to_feet(1, reverse=True)
    assert convert_unit(1,'yd','in') == inches_to_yards(1, reverse=True)

    assert convert_unit(1,'ft','in') != inches_to_feet(1.01, reverse=True)
    assert convert_unit(1,'yd','in') != inches_to_yards(1.01, reverse=True)
