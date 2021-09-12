def wave(s):
    fun = lambda i, s: "{}{}{}".format(s[:i],s[i].upper(),s[i+1:])
    return [*filter(lambda x: x != s, [fun(i, s) for i in range(len(s))])]