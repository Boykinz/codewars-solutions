from itertools import cycle

def swap(s, n):
    n = iter(cycle(bin(n)[2:]))
    s2 = [int(next(n)) if l.isalpha() else 0 for l in s]
    return ''.join((l, l.swapcase())[s2[i]] for i, l in enumerate(s))