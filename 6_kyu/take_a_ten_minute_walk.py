def is_valid_walk(walk):
    complex = {'w': -1, 'e': 1, 'n': 1j, 's': -1j}
    return (False, True)[len(walk)==10 and sum(map(complex.get, walk))==0]