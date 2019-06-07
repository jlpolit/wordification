import unittest
from wordification.wordification import number_to_words, words_to_number, all_wordifications


class TestWordificationFunctions(unittest.TestCase):
    def test_number_to_words(self):
        return True

    def test_words_to_number(self):
        # test some cases with various formatting and word/number mixtures
        valid_numbers = ['1-800-CAT-NAPS',
                         '888-NODASHS',
                         '1-999-999-9999',
                         '9LETTERSOY']
        self.assertEqual(words_to_number(valid_numbers[0]), '1-800-228-6277')
        self.assertEqual(words_to_number(valid_numbers[1]), '888-663-2747')
        self.assertEqual(words_to_number(valid_numbers[2]), '1-999-999-9999')
        self.assertEqual(words_to_number(valid_numbers[3]), '953-883-7769')
        # make sure we're catching invalid numbers
        self.assertRaises(ValueError, words_to_number, 'not a number in any way')

    def test_all_wordifications(self):
        return True


if __name__ == '__main__':
    unittest.main()
