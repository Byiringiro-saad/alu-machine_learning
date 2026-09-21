#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix.

    Args:
        matrix (list of lists): the matrix whose determinant should be
            calculated.

    Returns:
        The determinant of matrix.
    """
    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(sub)

    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix.

    Args:
        matrix (list of lists): the matrix whose minor matrix should be
            calculated.

    Returns:
        The minor matrix of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    result = []
    for i in range(n):
        result_row = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            result_row.append(determinant(sub))
        result.append(result_row)

    return result


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix.

    Args:
        matrix (list of lists): the matrix whose cofactor matrix should be
            calculated.

    Returns:
        The cofactor matrix of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.
    """
    minor_matrix = minor(matrix)

    return [[value * (-1) ** (i + j) for j, value in enumerate(row)]
            for i, row in enumerate(minor_matrix)]


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix.

    Args:
        matrix (list of lists): the matrix whose adjugate matrix should be
            calculated.

    Returns:
        The adjugate matrix of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.
    """
    cofactor_matrix = cofactor(matrix)

    return [list(row) for row in zip(*cofactor_matrix)]
