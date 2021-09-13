def longest_consec(s, k):
    if not 0 < k <= len(s):
        return ''
    return max([''.join(s[i:i+k]) for i in range(len(s)-k+1)], key=len)