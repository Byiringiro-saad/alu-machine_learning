#!/usr/bin/env python3
"""Module for concatenating two matrices along a specific axis."""


def matrix_shape(matrix):
    """Calculate the shape of a matrix as a list of integers."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def deep_copy(matrix):
    """Return a deep copy of a matrix."""
    if isinstance(matrix, list):
        return [deep_copy(element) for element in matrix]
    return matrix


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis, returning a
    new matrix."""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    if len(shape1) != len(shape2) or axis >= len(shape1):
        return None
    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None
    if axis == 0:
        return [deep_copy(row) for row in mat1] + \
            [deep_copy(row) for row in mat2]
    return [cat_matrices(m1, m2, axis - 1) for m1, m2 in zip(mat1, mat2)]
