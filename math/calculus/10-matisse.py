#!/usr/bin/env python3
"""Module that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial

    Args:
        poly: list of coefficients, where the index of each coefficient
            is the power of x it belongs to

    Returns:
        a new list of coefficients representing the derivative,
        [0] if the derivative is 0, or None if poly is not valid
    """
    if type(poly) is not list or len(poly) == 0:
        return None
    for coef in poly:
        if type(coef) not in (int, float):
            return None
    derivative = [i * poly[i] for i in range(1, len(poly))]
    if all(coef == 0 for coef in derivative):
        return [0]
    return derivative
