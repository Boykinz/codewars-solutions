def fold_array(arr, runs):
    for i in range(runs):
        n = len(arr) // 2
        x = [arr[i] + arr[-1-i] for i in range(n)] + [arr[n]]*(len(arr)%2)
        arr = x.copy()
    return arr