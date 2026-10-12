#!/usr/bin/env python3
"""Module that defines a Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Initializes the distribution from a data set

        Args:
            data: numpy.ndarray of shape (d, n) containing the data set
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        n = data.shape[1]
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.matmul(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point

        Args:
            x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
            the value of the PDF
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if x.ndim != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        deviation = x - self.mean
        exponent = np.matmul(
            np.matmul(deviation.T, np.linalg.inv(self.cov)), deviation)
        denominator = np.sqrt((2 * np.pi) ** d * np.linalg.det(self.cov))
        return float(np.exp(-exponent[0][0] / 2) / denominator)
