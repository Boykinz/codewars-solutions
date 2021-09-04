def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def perimeter(n):
    return 4 * sum(fibonacci(n+1))