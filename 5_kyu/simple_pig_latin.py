from re import findall

def pig_it(string):
    string, s2 = string.split(' '), ''
    for w in string:
        if findall(r'\w+', w): s2 += w[1:]+w[0]+'ay '
        else: s2 += w + ' '
    return s2[:-1]