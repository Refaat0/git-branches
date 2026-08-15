# This library exports basic mathematical functions
# Author: Refaat || Version: 1.0

#### Version 1.0 functions ####
def add(x, y):
    """ Returns the sum of two components

    Args:
        x (float) A component
        y (float) Another component to add to x

    Returns:
        float: The sum of the two components
    """
    return x+y

def substract(x, y):
    """ Returns the difference of two components

    Args:
        x (float) A component
        y (float) Another component to subtract from x

    Returns:
        float: The difference of the components
    """
    return x - y

def multiply(x, y):
    """ Returns the product of two components

    Args:
        x (float) A component
        y (float) Another component to multiply x by

    Returns:
        float: The product of two components
    """
    return x * y

def divide(x, y):
    """ Returns the quotient of two components

    Args:
        x (float) A component
        y (float) Another component to divide x by

    Returns:
        float: The quotient of two components

    Raises:
        ZeroDivisionError: When the y component is zero
    """

    if (y == 0):
        raise ZeroDivisionError("Cannot divide by zero")

    return x / y
