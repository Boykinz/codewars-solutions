def max_sequence(array):
    s = sum(array)
    for i in range(1, len(array) + 1):
        for j in range(0, len(array) - i + 2):
            new_s = sum(array[j:(j+i-1)])
            if new_s > s: s = new_s
    return s