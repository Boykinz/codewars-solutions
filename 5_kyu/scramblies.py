def scramble(s1, s2):
    for let in set(s2):
        if s1.count(let) < s2.count(let):
            return False
    return True