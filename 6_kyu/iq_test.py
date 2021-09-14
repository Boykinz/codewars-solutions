def iq_test(s):
    mods = [*map(lambda x: int(x)%2, s.split())]
    return mods.index(sum(mods[:3]) <= 1) + 1