from numpy import prod

def persistence(n, i=0):
    return i if n < 10 else persistence(prod(list(map(int, str(n)))), i+1)