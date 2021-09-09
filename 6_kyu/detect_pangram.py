from string import ascii_lowercase as alf
is_pangram = lambda s: not set(alf) - set(s.lower())