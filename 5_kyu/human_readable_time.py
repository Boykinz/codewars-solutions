def make_readable(n):
    return  "{:02d}".format(n//3600) + ':' + "{:02d}".format(n//60%60) + ':' + "{:02d}".format(n%60)