import wordification.helpers as helpers
import pandas as pd


def number_to_words(phone_num: str) -> str:
    """
    assumption: a valid wordification can be one word of 3 or more letters,
    or a 1-2 letter word followed by a longer word
    :param phone_num: a string representation of a phone number
    :return: a valid wordification of that number
    """
    character_list = helpers.get_character_list(phone_num)

    raise NotImplementedError


def words_to_number(phone_words: str) -> str:
    """

    :param phone_words: a string representation of a phone number that mixes words and digits
    :return: the number corresponding to this phone #
    """
    # drop hyphens, put everything into a list
    character_list = helpers.get_character_list(phone_words)
    out_list = []
    for c in character_list:
        if c.isdigit():
            out_list.append(c)
        else:
            out_list.append(helpers.numbers_from_letters_lookup[c.upper()])

    return helpers.format_phone_number(out_list)


def all_wordifications(phone_num: str) -> str:
    character_list = helpers.get_character_list(phone_num)
    combos = helpers.all_combinations(character_list)
    combo_df = pd.DataFrame()
    combo_df['potential_word'] = combos
    combo_df['has_word'] = combo_df.potential_word.apply(lambda x: helpers.has_valid_word(x))
    valid_combo_df = combo_df[combo_df.has_word == True]
    return valid_combo_df.potential_word.apply(lambda x: helpers.format_wordification(x))
