from collections import Counter

def find_uniq(arr):
    for k, v in Counter(arr).items():
        if v == 1:
            return k