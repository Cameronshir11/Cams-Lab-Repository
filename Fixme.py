#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    if n > 0:
        xs = filter(lambda n: n % 2 == 0, range(n + 1))
        xs = list(xs)
        return xs
    elif n < 0:
        xs = []
        xs = list(xs)
        return xs
    else:
        xs = [0]
        return xs
