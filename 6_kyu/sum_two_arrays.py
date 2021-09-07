def sum_arrays(array1,array2):
    if not (array1 or array2):
        return []
    elif not (array1 and array2):
        if len(array1) == 1:
            return array1
        elif len(array2) == 1:
            return array2
        elif array1:
            return array1 if array1[0] else array1[1:]
        else:
            return array2 if array2[0] else array2[1:]
    num1, num2 = ''.join(map(str, array1)), ''.join(map(str, array2))
    x = str(int(num1) + int(num2))[0] == '-'
    s = str(int(num1) + int(num2)).replace('-', '')
    z = [*map(int, s)]
    z[0] = (1, -1)[x] * z[0]
    return z