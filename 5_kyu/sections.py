from math import modf, sqrt

def c(q):
    r = s = 1
    if modf(sqrt(q))[0]: return 0
    while s * s < q:
        c, s = 0, -~s
        while q % s < 1: c, q = -~c, q // s
        r *= 1 + c * 3 // 2
    return not 1 - q and r