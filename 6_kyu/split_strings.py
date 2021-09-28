def solution(s):
    s = s + '_' if len(s)%2 else s
    return [s[i] + s[i+1] for i in range(0, len(s), 2)]