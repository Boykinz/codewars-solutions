def string_letter_count(s):
    array = [(str(s.lower().count(i)), i) for i in s.lower() if i.isalpha()]
    return ''.join(c[0]+c[1] for c in sorted(set(array), key=lambda x: x[1]))