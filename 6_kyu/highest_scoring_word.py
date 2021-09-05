from string import ascii_lowercase as alf

def high(s):
    x, n = s.split(' '), []
    for word in x:
        n.append(sum(map(lambda a: alf.index(a)+1, word)))
    return x[n.index(max(n))]