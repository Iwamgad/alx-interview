#!/usr/bin/python3
"""This module contains a function that returns the fewest number of 
    operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly 
    n H characters in the file.
    """
    now = 1
    start = 0
    count = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            count += 2
        else:
            now += start
            count += 1

    return count

