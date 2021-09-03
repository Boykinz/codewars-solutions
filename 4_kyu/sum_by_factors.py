from functools import reduce
from operator import mul


def prime_factors(n):
    i, f, n = 2, [], abs(n)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            f.append(i)
            n //= i
    return f + [n] if n > 1 else f


def sum_for_list(lst):
    auf = []
    arr = list(map(prime_factors, lst))
    sarr = set([i for f in arr for i in f])
    sign = list(map(lambda x: (1, -1)[x < 0], lst))
    for el in sarr:
        s = 0
        for item, er in zip(arr, sign):
            if el in item:
                s += reduce(mul, item) * er
        auf.append([el, s])
    return sorted(auf, key=lambda x: x[0])
