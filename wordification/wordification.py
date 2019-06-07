import wordification.helpers as helpers


def number_to_words(phone_num: str) -> str:
    raise NotImplementedError


def words_to_numbers(phone_words: str) -> str:
    """

    :param phone_words: a string representation of a phone number that mixes words and digits
    :return: the number corresponding to this phone #
    """
    # drop hyphens, put everything into a list
    character_list = [x for x in phone_words.replace('-', '')]
    out_list = []
    for c in character_list:
        if c.isdigit():
            out_list.append(c)
        else:
            out_list.append(helpers.numbers_from_letters_lookup[c.upper()])

    return helpers.format_phone_number(out_list)


def all_wordifications(phone_num: str) -> str:
    raise NotImplementedError



