from re import findall, search
from collections import OrderedDict

def top_3_words(text):
    array = findall("[\'a-z]+", text.lower())
    array = [*filter(lambda z: search(r'\w', z), array)]
    f = list(OrderedDict.fromkeys(array))
    return sorted(f, key=array.count, reverse=True)[:3]