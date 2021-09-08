from random import randint
from re import match

squares = lambda n: [x**2 for x in range(1, n+1)]
num_range = lambda n, start, step: [*range(start, step*n+start, step)]
rand_range = lambda n, mn, mx: [randint(mn, mx) for i in range(n)]

def is_prime(n):
    return match(r'^1?$|^(11+?)\1+$', '1' * n) is None

def primes(n):
    lst, i = [], 2
    while len(lst) < n:
        if is_prime(i):
            lst.append(i)
        i += 1
    return lst