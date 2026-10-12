#!/usr/bin/env python3
"""Module that defines a Binomial distribution"""


class Binomial:
    """Represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the distribution from data or given parameters"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - variance / mean
            self.n = int(round(mean / p))
            self.p = float(mean / self.n)

    @staticmethod
    def factorial(x):
        """Calculates the factorial of x as a float"""
        result = 1.
        for i in range(1, x + 1):
            result *= i
        return result

    def pmf(self, k):
        """Calculates the value of the PMF for k successes"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        combinations = self.factorial(self.n) / (
            self.factorial(k) * self.factorial(self.n - k))
        return combinations * self.p ** k * (1 - self.p) ** (self.n - k)

    def cdf(self, k):
        """Calculates the value of the CDF for k successes"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
