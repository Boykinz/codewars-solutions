from collections import OrderedDict

def format_duration(n):

    if n == 0: 
        return 'now'

    data = OrderedDict([
                     ('year', n // (31536000)), 
                     ('day', n % (31536000) // (86400)),
                     ('hour', n % (31536000) % (86400) // (3600)),
                     ('minute', n % (31536000) % (86400) % (3600) // 60),
                     ('second', n % (31536000) % (86400) % (3600) % 60)
                   ])

    answer = str()
    for k, v in data.items():
        if v == 0: continue
        elif v == 1: answer += "1 " + k + ", "
        else: answer += str(v) + " " + k + "s, "

    answer = answer[:len(answer)-2]
    return (answer[::-1].replace(',', 'dna ', 1))[::-1]