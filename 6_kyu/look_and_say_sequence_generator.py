from itertools import groupby

def look_and_say_sequence(string, N):
    if N == 1:
        return string
    return look_and_say_sequence(''.join(str(len(list(g))) + key for key, g in groupby(string)), N - 1)