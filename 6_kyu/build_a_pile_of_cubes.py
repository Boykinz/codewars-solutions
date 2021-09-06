def find_nb(m):
    x, i = 0, 0
    while x < m:
        i += 1
        x += i ** 3
    return i if x == m else -1