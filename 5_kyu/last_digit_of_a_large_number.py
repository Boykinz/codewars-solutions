def last_digit(a, b):
    x = 1
    while b > 0:
        if b % 2 == 1:
            x = (x * a) % 10
        a *= a % 10
        b //= 2   
    return x