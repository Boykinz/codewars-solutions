def dig_pow(n, p):
    num = sum(map(lambda x: int(x[1])**x[0], enumerate(str(n),p)))
    return -1 if num % n else num // n