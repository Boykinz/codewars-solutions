from collections import Counter as C

def duplicate_count(text):
    return sum(1 for item in C(text.lower()) if C(text.lower())[item] > 1)