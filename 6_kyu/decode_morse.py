def decode(s):
    y = lambda x: TOME[x] if x in TOME else ' '
    return (s, ''.join([*map(y, s.split(' '))]))[bool(s)]