def group_by_commas(n):
    s, k = '', str(n)[::-1]
    for i, d in enumerate(k, 1):
        s += d + ',' * (not i % 3 and i != len(k))
    return s[::-1]