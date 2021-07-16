from impyrial.weight.core import (
    UNITS,
    ounces_to_pounds,
    ounces_to_stone
)

# Define tests for ounces_to_pounds function
def test_weight_ounces_to_pounds():
	# Check that 12 inches is converted to 1 foot
    assert ounces_to_pounds(12) == 1.0
    # Check that 2.5 feet is converted to 30 inches
    assert ounces_to_pounds(2.5, reverse=True) == 30.0


# Define tests for ounces_to_stone function
def test_weight_ounces_to_stone():
	# Check that 12 inches is converted to 1 foot
    assert ounces_to_stone(12) == 1.0
    # Check that 2.5 feet is converted to 30 inches
    assert ounces_to_stone(2.5, reverse=True) == 30.0