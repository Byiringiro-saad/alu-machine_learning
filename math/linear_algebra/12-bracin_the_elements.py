#!/usr/bin/env python3
"""Module for element-wise matrix arithmetic."""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication,
    and division."""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
