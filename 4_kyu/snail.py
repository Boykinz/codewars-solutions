from itertools import cycle

def snail(a):
    step = ['a', 'b', 'c', 'd']
    pool, x = cycle(step), []
    for item in pool:
        if a == []:
            return x
        elif item == 'a':
            for elem in a[0]:
                x.append(elem)
            a.pop(0)
        elif item == 'b':
            for i in range(len(a)):
                x.append((a[i])[-1])
                (a[i]).pop(-1)
        elif item == 'c':
            for elem in (a[-1])[::-1]:
                x.append(elem)
            a.pop(-1)
        elif item == 'd':
            for i in range(len(a)-1, -1, -1):
                x.append((a[i])[0])
                (a[i]).pop(0)