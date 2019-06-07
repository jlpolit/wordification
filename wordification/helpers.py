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


def is_valid_word(word_to_check, min_length=1):
    if type(word_to_check) is not str:
        raise ValueError("Non-string entered")
    if len(word_to_check) < min_length:
        return False
    else:
        english_word_lookup = enchant.Dict("en_US")
        return english_word_lookup.check(word_to_check)

