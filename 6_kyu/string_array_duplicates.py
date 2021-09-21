from re import sub

def dup(arry):
    return [sub(r'([a-z])\1+', r'\1', s) for s in arry]