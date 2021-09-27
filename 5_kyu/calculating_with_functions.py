def zero(x = None):
    if x == None: return 0
    else: return x(0)

def one(x = None): 
    if x == None: return 1
    else: return x(1)

def two(x = None):
    if x == None: return 2
    else: return x(2)

def three(x = None): 
    if x == None: return 3
    else: return x(3)

def four(x = None): 
    if x == None: return 4
    else: return x(4)

def five(x = None):
    if x == None: return 5
    else: return x(5)

def six(x = None):
    if x == None: return 6
    else: return x(6)

def seven(x = None):
    if x == None: return 7
    else: return x(7)

def eight(x = None):
    if x == None: return 8
    else: return x(8)

def nine(x = None):
    if x == None: return 9
    else: return x(9)

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: int(x / y)