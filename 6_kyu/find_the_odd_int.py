def find_it(x):
    for item1 in x:
        i = 0
        for item2 in x:
            if item1 == item2: i += 1
        if i % 2 != 0: return item1