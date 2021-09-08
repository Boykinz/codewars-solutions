def longest_repetition(chars):
    if not chars:
        return ('', 0)
    x = [[chars[0], 1]]
    for char in chars[1:]:
        if x[-1][0] == char:
            x[-1][1] += 1
        else:
            x.append([char, 1])
    return tuple(max(x, key=lambda x: x[1]))