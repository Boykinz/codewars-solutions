def find_outlier(arr):
    mods = [n % 2 for n in arr]
    return arr[mods.index(0)] if sum(mods[:3]) > 1 else arr[mods.index(1)]