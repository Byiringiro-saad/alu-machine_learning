#!/usr/bin/env python3
"""Module that defines a Normal distribution"""


class Normal:
    """Represents a normal distribution"""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the distribution from data or given parameters"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        coefficient = 1 / (self.stddev * (2 * Normal.pi) ** 0.5)
        return coefficient * Normal.e ** (-0.5 * self.z_score(x) ** 2)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        v = (x - self.mean) / (self.stddev * 2 ** 0.5)
        erf = v - v ** 3 / 3 + v ** 5 / 10 - v ** 7 / 42 + v ** 9 / 216
        erf *= 2 / 3.14159265359 ** 0.5
        return 0.5 * (1 + erf)
