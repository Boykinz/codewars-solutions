from math import sqrt

def list_squared(m, n):
    x = []
    for num in range(m, n + 1):
        i, s = 2, [1, num ** 2]
        while i < sqrt(num):
            if num % i == 0:
                s.append(i ** 2)
                s.append((num // i) ** 2)
            i += 1
        base = sum(s)
        if sqrt(base).is_integer():
            x.append([num, base])
    return [[1, 1]] + x if m == 1 else x