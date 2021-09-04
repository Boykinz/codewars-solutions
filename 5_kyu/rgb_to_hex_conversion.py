def rgb(r, g, b):
    y = lambda x: x if -1 < x < 256 else (0, 255)[x > 255]
    return ''.join('{:02x}'.format(i).upper() for i in map(y, (r, g, b)))