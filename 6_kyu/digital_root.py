def digital_root(n):
    n = sum(int(i) for i in str(n))
    return n if n < 10 else digital_root(n)