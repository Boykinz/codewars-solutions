import re


def uncollapse(digits):
    words = [
        'zero', 'one', 'two', 'three',
        'four', 'five', 'six',
        'seven', 'eight', 'nine'
    ]
    pattern = '|'.join(words)
    regex = re.compile(pattern)
    return ' '.join(regex.findall(digits))
