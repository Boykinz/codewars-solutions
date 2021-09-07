from numpy import prod

def solve(arr):
    return prod([*map(lambda x: len(set(x)), arr)])