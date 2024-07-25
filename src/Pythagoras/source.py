# Requirements Gathering

# 2 inputs, Positive, integer or float (is digit)
# 1 output, float
# external library? No external library
# create a function - calculate hypot = sqrt(a^2 + b^2)

def hypot(a, b):
    #docstring
    """This is a hypot function that works by selecting the absolute value and returning the square root value.

    Args:
        a (int, float):First side of triangle
        b (int, float): Second side of triangle

    Returns:
        float: hypotenuse
    """
    return sqrt(a**2 + b**2)

# Create a square root function : positive number - returns a float
def sqrt (a):
    """Square root function

    Args:
        a (int, float): Positive or negative numbers

    Returns:
        float: square root value
    """
    #return 2.0
    return abs(a**0.5)

#print(sqrt(4))
#print(hypot(3,4))

