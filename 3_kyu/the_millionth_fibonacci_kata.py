import numpy as np

def fib(n):

    if abs(n) < 2:
        return n
    elif (n < 0) and (n % 2 == 0):
        return -(pow(np.matrix([[1, 1], [1, 0]], dtype=object), -n-1))[0, 0]
    else:
        return (pow(np.matrix([[1, 1], [1, 0]], dtype=object), abs(n)-1))[0, 0]