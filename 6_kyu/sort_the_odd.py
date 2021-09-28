def sort_array(source_array):
    arr = sorted([i for i in source_array if i%2])
    replace = lambda x: x if not x%2 else arr.pop(0)
    return list(map(replace, source_array))