from math import modf, sqrt, floor

def solve(n):
    i = floor(sqrt(n))
    z = (n//i - i)**2 // 4 if (n//i - i)**2 // 4 > 0 else 1
    while modf(sqrt(z + n))[0] and i > 1:
        i -= 1
        z = (n//i - i)**2 // 4
    return z if not modf(sqrt(z + n))[0] else -1