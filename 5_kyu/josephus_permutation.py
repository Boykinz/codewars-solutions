def josephus(n, k):
    i, arr = 0, []
    while len(n) > 1:
        i = (i + k - 1) % len(n)
        arr.append(n.pop(i))
    return arr + n