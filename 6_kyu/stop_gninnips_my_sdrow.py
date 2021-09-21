def spin_words(s):
    return ' '.join((l, l[::-1])[len(l) > 4] for l in s.split())
