#!/usr/bin/env python3
"""This script creates a Pascal Triangle"""


def pascal_triangle(n):
    """
      Returns a list of lists of integers representing
      the Pascal’s triangle of n
    """
    if type(n) is not int or n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
