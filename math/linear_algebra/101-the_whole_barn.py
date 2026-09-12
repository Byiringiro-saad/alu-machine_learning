#!/usr/bin/env python3
"""Module for adding two matrices of arbitrary dimension."""


def matrix_shape(matrix):
    """Calculate the shape of a matrix as a list of integers."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def add_matrices(mat1, mat2):
    """Add two matrices of the same shape, returning a new matrix."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    if isinstance(mat1, list):
        return [add_matrices(a, b) for a, b in zip(mat1, mat2)]
    return mat1 + mat2
