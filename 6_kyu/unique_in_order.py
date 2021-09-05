def unique_in_order(s):
    arr = []
    if len(s) <= 1:
        return list(s)
    for j, let in enumerate(s[:-1]):
        if let != s[j+1]:
            arr.append(let)
    return arr + [s[-1]]