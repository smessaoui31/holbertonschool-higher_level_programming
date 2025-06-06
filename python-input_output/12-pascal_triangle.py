#!/usr/bin/python3
"""
Returns Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
        triangle.append(row)
    return triangle
