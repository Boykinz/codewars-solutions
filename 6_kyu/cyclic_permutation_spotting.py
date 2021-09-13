def is_cyclic(p, n=-1, x=None):

    if n == -1:
        x = [0]
        n = len(p[0])

    if n == 0:
        if len(set(x)) == len(p[0]):
            return True
        else:
            return False

    x.append(p[0].index(p[1][x[-1]]))

    return is_cyclic(p, n-1, x)