"""
A collection of simple math operations
"""


def simple_add(a, b):
    """Return the sum of two numbers."""
    return a+b


def simple_sub(a, b):
    """Return the difference between two numbers."""
    return a-b


def simple_mult(a, b):
    """Return the product between two numbers."""
    return a*b


def simple_div(a, b):
    """Return the quotient between two numbers."""
    return a/b


def poly_first(x, a0, a1):
    """
    Evaluate a first degree polynomial at values 'x'.

    Parameters
    ----------
    x : array_like
        Independent variable.
    a0 : int, float
        Constant coefficient.
    a1 : int, float
        Linear coefficient.

    Returns
    -------
    ndarray


    """
    return a0 + a1*x


def poly_second(x, a0, a1, a2):
    """
    Evaluate a second degree polynomial at values 'x'.

    Parameters
    ----------
    x : array_like
        Independent variable.
    a0 : int, float
        Constant coefficient.
    a1 : int, float
        Linear coefficient.
    a2 : int, float
        Quadratic coefficient.

    Returns
    -------
    ndarray
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
