import operator

class Calculator:
    op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

    def __init__(self):
        self.result = []

    def evaluate(self, string):
        self.result = string.split(' ')
        self.loop('*/')
        self.loop('+-')
        return float(self.result[0])

    def loop(self, op):
        i = 1
        while i < len(self.result) - 1:
            if self.result[i] in op:
                self.result[i - 1] = str(self.__class__.op[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i + 1)
                self.result.pop(i)
                continue
            i += 1