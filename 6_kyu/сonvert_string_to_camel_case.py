def to_camel_case(text):
    if not text:
        return ''
    text = text.replace('-','_').split('_')
    return ''.join([text[0]] + [i.title() for i in text[1:]])