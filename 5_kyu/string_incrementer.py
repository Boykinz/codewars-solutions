from re import match

def increment_string(s):
    y = lambda k: match(r'[0-9]+', k[::-1])
    z = lambda m: str(int(m[::-1])+1).zfill(len(m))
    x = y(s).group(0) if y(s) is not None else ''
    return s.replace(x[::-1], '') + (z(x) if x else '1')