from string import ascii_lowercase as alf

def alphabet_position(text):
    mask = dict((j, i) for i, j in enumerate(alf, 1))
    return ' '.join(str(mask[l]) for l in text.lower() if l in mask)