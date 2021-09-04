def first_non_repeating_letter(string):
    for char in string.lower():
        if string.lower().count(char) == 1:
            return string[string.lower().index(char)]
    return ''