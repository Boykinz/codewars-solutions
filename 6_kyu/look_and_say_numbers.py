from itertools import groupby
from copy import copy


def look_and_say(data='1', maxlen=5, lst=[]):
    
    if maxlen == 0:
        x = lst.copy()
        lst.clear()
        return x
    
    x = list()
    for k, v in groupby(data):
        x.extend([str(len([*v])), k])
    lst.append(''.join(x))
    
    return look_and_say(x, maxlen-1, lst)