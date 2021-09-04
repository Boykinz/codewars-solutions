def zeros(n):
    s, x = 0, 5
    while x < n:
        s += n // x
        x *= 5
    return s