#!/usr/bin/env python3
"""Module that calculates a continuous posterior probability"""
from scipy import special


def posterior(x, n, p1, p2):
    """Calculates the posterior probability that p is within a range

    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        p1: lower bound on the range
        p2: upper bound on the range

    Returns:
        the posterior probability that p is within the range [p1, p2]
        given x and n
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or p1 < 0 or p1 > 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or p2 < 0 or p2 > 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    a = x + 1
    b = n - x + 1
    integral1 = p1 ** a * special.hyp2f1(a, 1 - b, a + 1, p1) / a
    integral2 = p2 ** a * special.hyp2f1(a, 1 - b, a + 1, p2) / a
    probability = (integral2 - integral1) * (1 / special.beta(a, b))
    if probability < 0:
        return probability - probability
    return probability
