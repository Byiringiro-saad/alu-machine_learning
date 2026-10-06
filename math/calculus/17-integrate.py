#!/usr/bin/env python3
"""Module that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial

    Args:
        poly: list of coefficients, where the index of each coefficient
            is the power of x it belongs to
        C: integer representing the integration constant

    Returns:
        a new list of coefficients representing the integral,
        or None if poly or C is not valid
    """
    if type(poly) is not list or len(poly) == 0:
        return None
    if type(C) not in (int, float):
        return None
    for coef in poly:
        if type(coef) not in (int, float):
            return None
    integral = [C]
    for power, coef in enumerate(poly):
        value = coef / (power + 1)
        if value == int(value):
            value = int(value)
        integral.append(value)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
