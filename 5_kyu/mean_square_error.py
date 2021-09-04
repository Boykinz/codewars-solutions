def solution(a, b):
    return sum((j-i)**2 for i, j in zip(a, b))/len(a)