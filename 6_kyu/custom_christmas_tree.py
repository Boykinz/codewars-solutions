from itertools import cycle

def custom_christmas_tree(chars, n):
    itr, string = iter(cycle(chars)), ''
    for i in range(1, n+1):
        string += ' '*(n-i) + ' '.join(next(itr) for _ in range(i)) + '\n'
    string += (' '*(n-1) + '|' + '\n') * (n//3 - 1)
    string += ' '*(n-1) + '|'
    return string