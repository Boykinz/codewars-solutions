from itertools import accumulate

parts_sums = lambda ls: [*accumulate(ls[::-1])][::-1] + [0]