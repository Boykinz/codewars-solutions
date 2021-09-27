def all_fibonacci_numbers(a = 1, b = 0):
    while True:
        yield a
        a, b = b + a, a