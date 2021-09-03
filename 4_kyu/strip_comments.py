def solution(string, markers):
    string = string.split('\n')
    for m in markers:
        for i, s in enumerate(string):
            if m in s:
                string[i] = string[i][:string[i].index(m)].strip()
    return  '\n'.join(string)