import math


def combination(n, r):
    """
    :param n: number of objects
    :param r: size of a subset
    :return: number of r-combinations of n objects
    """
    if n < r:
        return 0
    else:
        return math.factorial(n)/math.factorial(n-r)/math.factorial(r)

