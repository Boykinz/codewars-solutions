from string import ascii_lowercase, ascii_uppercase

def rot13(string):
    x = dict(zip(ascii_lowercase, ascii_lowercase[13:]+ascii_lowercase[:-13]))
    x.update(dict(zip(ascii_uppercase, ascii_uppercase[13:]+ascii_uppercase[:-13])))
    return ''.join(list(map(lambda z: x[z] if z in x else z, string)))