import enchant
import re
import itertools

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

english_word_lookup = enchant.Dict("en_US")


# TODO: it might make sense to allow 'I' and 'a' with the stipulation that they be followed by a valid word...
def is_valid_word(word_to_check: str,
                  min_length=2,
                  exceptions=list()) -> bool:
    if type(word_to_check) is not str:
        raise ValueError("Non-string entered")
    if (len(word_to_check) < min_length) and (word_to_check not in exceptions):
        return False
    else:
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


def get_character_list(phone_words: str) -> list:
    if type(phone_words) is not str:
        raise ValueError("Not a Valid Input")
    return [x for x in re.sub('\W+', '', phone_words)]


def all_values_from_number(num: str) -> list:
    letters = letters_from_numbers_lookup.get(num, [num])
    if num not in letters:
        letters += [num]
    return letters


def all_combinations(number_list: list) -> list:
    """

    :param number_list: array of strings representing digits between 0 and 9
    :return: all possible number-letter combinations
    """
    all_chars = [all_values_from_number(x) for x in number_list]
    # note: I broke this out for ease of testing,
    # but really we'd want this to return the iterable for efficiency
    return list(itertools.product(*all_chars))


def has_valid_word(char_list: list) -> bool:
    """

    :param char_list: array of strings, can be combination of digits and letters
    :return: whether there is a valid English word in this array, based on the letters in order
    note that this word must be surrounded on both sides by numbers (1800-PAINTX is not a valid word)
    """
    phone_number = ''.join(char_list)
    only_letters = re.sub("\d", " ", phone_number)
    letters_split = only_letters.split(' ')
    for sub_word in letters_split:
        if len(sub_word) > 2:
            if is_valid_word(''.join(sub_word)):
                return True
    return False


def format_wordification(char_list: list) -> str:
    """

    :param char_list: letter-number combination in an array (all strings)
    :return: valid wordification with dashes between any letter/number chunks
    """
    out = ''
    n = len(char_list)
    char_str = ''.join(char_list)
    num_letter_list = re.split('(\d+)', char_str)
    if len(num_letter_list) == 3:
        out = format_phone_number(char_list)
    else:
        for chunk in num_letter_list:
            if chunk in ['', ' ']:
                pass
            else:
                out += chunk
                out += '-'
        out = out[:-1]
        if (n == 11) and (char_list[0] == '1') and(out[1] != '-'):
            out = '1-' + out[1:]
    return out
