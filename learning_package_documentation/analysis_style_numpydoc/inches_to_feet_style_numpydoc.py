INCHES_PER_FOOT = 12.0  # 12 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """
    Terminal command | pyment -w -o numpydoc inches_to_feet.py
    Flags
    -w          | overwrite
    -o <style>  | styleput in NumPy Documentation style

    Convert lengths between inches and feet

    Parameters
    ----------
    x : numpy.ndarray
        Lengths in feet
    reverse : bool, optional
        If true this function converts from feet to inches
        instead of the default behavior of inches to feet
        (Default value = False)

    Returns
    -------
    numpy.ndarray


    [According documentation style 'numpydoc' at MODULE level]

    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT
