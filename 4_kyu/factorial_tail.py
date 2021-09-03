from math import log

def zeroes(base, number):
    z, f = 0, 1
    b = base ** round(log(1000001, base))
    for i in range(2, number + 1):
        f *= i
        while f % base == 0:
            f //= base
            z += 1
        f %= b
    return z