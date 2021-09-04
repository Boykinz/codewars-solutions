from math import sqrt

def sol_equa(n):
    arr = []
    for a in range(1, int(sqrt(n))+2):
        if n % a == 0:
            b = n // a
            x = (a + b) // 2
            y = (b - a) // 4
            if x**2 - 4*y**2 == n:
                arr.append([x, y])
    return arr