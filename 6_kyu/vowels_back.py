from string import ascii_lowercase as alf


def vowel_back(s1):
    
    s2 = ''
    f1 = {j: i for i, j in enumerate(alf)}
    f2 = {v: k for k, v in f1.items()}
    
    for l in s1:
        if l == 'c' or l == 'o':
            s2 += f2[f1[l]-1]
        elif l == 'd':
            s2 += f2[f1[l]-3]
        elif l == 'e':
            s2 += f2[f1[l]-4]
        elif l in 'aeiou':
            x = f2[(f1[l]-5)%26]
            s2 += [x, l][x in 'code']
        else:
            x = f2[(f1[l]+9)%26]
            s2 += [x, l][x in 'code']
            
    return s2