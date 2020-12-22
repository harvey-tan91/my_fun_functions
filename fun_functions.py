
def to_hex(letter: str)-> str:
    unicode_letter = ord(letter)
    return hex(unicode_letter)


def string_to_hex(string: str)-> str:
    lst = list(string)
    return ''.join([to_hex(i)[-2:] for i in lst])


