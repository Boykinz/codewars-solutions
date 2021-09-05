def valid_word(seq, word):
    t = lambda x: sorted(x, reverse=True)
    for w in sorted(seq, key=t, reverse=True):
        if w in word:
            word = ''.join(word.split(w))
    return len(word) == 0