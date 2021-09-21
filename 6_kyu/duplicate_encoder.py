from collections import Counter as C

def duplicate_encode(word):
    return ''.join(('(', ')')[C(word.lower())[i] > 1] for i in word.lower())