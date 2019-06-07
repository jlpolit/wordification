import enchant
# derived from a google image search of an "old fashioned" phone
letters_from_numbers_lookup = {'2': ['A', 'B', 'C'],
                               '3': ['D', 'E', 'F'],
                               '4': ['G', 'H', 'I'],
                               '5': ['J', 'K', 'L'],
                               '6': ['M', 'N', 'O'],
                               '7': ['P', 'Q', 'R', 'S'],
                               '8': ['T', 'U', 'V'],
                               '9': ['W', 'X', 'Y' 'Z']}


numbers_from_letters_lookup = {'A': '2', 'B': '2', 'C': '2',
                               'D': '3', 'E': '3',  'F': '3',
                               'G': '4', 'H': '4',  'I': '4',
                               'J': '5', 'K': '5',  'L': '5',
                               'M': '6', 'N': '6', 'O': '6',
                               'P': '7', 'Q': '7', 'R': '7', 'S': '7',
                               'T': '8', 'U': '8', 'V': '8',
                               'W': '9', 'X': '9', 'Y': '9', 'Z': '9'}


def is_valid_word(word_to_check: str, min_length=1) -> bool:
    if type(word_to_check) is not str:
        raise ValueError("Non-string entered")
    if len(word_to_check) < min_length:
        return False
    else:
        english_word_lookup = enchant.Dict("en_US")
        return english_word_lookup.check(word_to_check)


def format_phone_number(phone_digit_list: list) -> str:
    #TODO: we should actually probably check that each 'digit' is a string rather than forcing it
    out_str = ''
    # length check
    if (len(phone_digit_list) not in [10, 11]) or (type(phone_digit_list) is not list):
        raise ValueError("not a valid phone number")
    # country code
    if len(phone_digit_list) == 11:
        out_str = (phone_digit_list.pop(0) + '-')

    # zipcode
    for digit in phone_digit_list[:3]:
        out_str += str(digit)
    out_str += '-'

    # the...next three digits (I'm sure this has a name)
    for digit in phone_digit_list[3:6]:
        out_str += str(digit)
    out_str += '-'

    # and the last four
    for digit in phone_digit_list[6:]:
        out_str += str(digit)

    return out_str
