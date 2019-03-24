import math


def permutation(n, r):
    """
    :param n: number of objects
    :param r: size of an ordered list
    :return: the number of r-permutation of n objects
    """
    if n < r:
        return 0
    else:
        return math.factorial(n) / math.factorial(n-r)

