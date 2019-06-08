import unittest
import wordification.helpers as helpers


class TestHelperFunctions(unittest.TestCase):
    def test_is_valid_word(self):
        # test some words with varying lowercase/uppercase mixes
        self.assertEqual(helpers.is_valid_word('DUCK'), True)
        self.assertEqual(helpers.is_valid_word('snow'), True)
        self.assertEqual(helpers.is_valid_word('disgustingly'), True)
        self.assertEqual(helpers.is_valid_word('Complicated'), True)
        # make sure our length limit works
        self.assertEqual(helpers.is_valid_word('cow', 4), False)
        # and that nonsense words are caught
        self.assertEqual(helpers.is_valid_word('fnnn'), False)
        # make sure errors are thrown when appropriate
        self.assertRaises(ValueError, helpers.is_valid_word, 5)
        # check our exception functionality
        self.assertEqual(helpers.is_valid_word('I', 2), False)
        self.assertEqual(helpers.is_valid_word('I', 2, ['I']), True)

    def test_format_phone_number(self):
        # test failure cases
        self.assertRaises(ValueError, helpers.format_phone_number, 'not a phone number')
        self.assertRaises(ValueError, helpers.format_phone_number, [1, 2, 3])
        # make sure 10 and 11 digit numbers are handled correctly
        base_number = [str(x) for x in [8,0,0,4,4,4,5,5,2,2]]
        number_with_country = ['1'] + base_number
        self.assertEqual(helpers.format_phone_number(base_number), '800-444-5522')
        self.assertEqual(helpers.format_phone_number(number_with_country), '1-800-444-5522')

    def test_get_character_list(self):
        self.assertEqual(helpers.get_character_list('800-444-5522'),
                         ['8', '0', '0', '4', '4', '4', '5', '5', '2', '2'])
        self.assertEqual(helpers.get_character_list('  INVALID  ## $$ ----'), ['I', 'N', 'V', 'A', 'L', 'I', 'D'])
        self.assertRaises(ValueError, helpers.get_character_list, 33)


if __name__ == '__main__':
    unittest.main()
