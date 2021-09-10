def order(sentence):
    place = lambda x: int(*filter(str.isdigit, x))
    return ' '.join(sorted(sentence.split(), key=place))