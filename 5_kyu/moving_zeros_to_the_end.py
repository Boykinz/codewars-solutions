def move_zeros(a):
    return [i for i in a if i is False or i != 0] + [j for j in a if j is not False and j == 0]