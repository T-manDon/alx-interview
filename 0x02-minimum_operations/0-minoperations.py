#!/usr/bin/python3
"""In a txt file, a single character H.
 the text editor can exe two operations
 in this file: Copy and Paste Giv num
n, write a method to calculates fewest number
of operations to result in exactly n H
char the file."""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
