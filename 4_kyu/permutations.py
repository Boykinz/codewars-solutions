from itertools import permutations as perm

permutations = lambda s: set([''.join(p) for p in perm(s)])