def beggars(arr, k):
    n, x = len(arr), [0] * k
    is_visited = set()
    for b in range(k):
        for i in range(b, n, k):
            if i in is_visited:
                continue
            else:
                x[b] += arr[i]
                is_visited.add(i)
    return x