def generate_hashtag(string):
    if string == '':
        return False
    else:
        string, h = string.split(' '), '#'
        length = 0
        for item in string:
            h += item.title()
            length += len(item)
            if length > 140:
                return False
        return h