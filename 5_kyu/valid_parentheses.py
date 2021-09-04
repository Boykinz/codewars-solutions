from re import findall

def valid_parentheses(string):
    y = 0
    for item in findall(r'[()]', string):
        y += {'(': 1, ')': -1}.get(item)
        if y < 0:
            return False
    return (False, True)[y == 0]