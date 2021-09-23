mor = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
       '--.': 'G',   '....': 'H',     '..': 'I',
       '.---': 'J',    '-.-': 'K',   '.-..': 'L',
       '--': 'M',     '-.': 'N',    '---': 'O',
       '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U',
       '...-': 'V',    '.--': 'W',   '-..-': 'X',
       '-.--': 'Y',   '--..': 'Z',  '-----': '0',
       '.----': '1',  '..---': '2',  '...--': '3',
       '....-': '4',  '.....': '5',  '-....': '6',
       '--...': '7',  '---..': '8',  '----.': '9',
       '': ' ', '...---...': 'SOS', '-.-.--':'!',
       '.-.-.-':'.'}


def decodeMorse(s):
    x = s.strip().split(' ')
    return ''.join([*map(lambda z: (z, mor[z])[z in x], x)]).replace('  ', ' ')