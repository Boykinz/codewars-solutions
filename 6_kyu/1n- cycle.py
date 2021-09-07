def cycle(n) :
    if (n % 2 == 0) or (n % 5 == 0):
        return -1
    i, k = 0, 1
    while True:
        k = k * 10 % n
        i += 1
        if k == 1: 
            return i