from numpy import matrix
from itertools import product

def valid_solution(array):
    a, dig = matrix(array), list(range(1, 10)) 
    ind = [(0, 1, 2), (3, 4, 5), (6, 7, 8)] 

    for i in range(len(a)): 
        if sorted(a[i].T) == sorted(a.T[i].T) == dig:
            continue 
        else:
            return False 

    for row, col in product(ind, ind): 
        b = [array[r][c] for r, c in product(row, col)] 
        if sorted(b) != dig:
            return False
    return True