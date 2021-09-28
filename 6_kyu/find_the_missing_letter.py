from string import ascii_letters as alf

def find_missing_letter(chars):
    ind = alf.index(chars[0])
    for a, b in zip(alf[ind:], chars):
        if a != b:
            return a