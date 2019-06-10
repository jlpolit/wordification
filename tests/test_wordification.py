import unittest
import random
from wordification.wordification import number_to_words, words_to_number, all_wordifications


class TestWordificationFunctions(unittest.TestCase):
    def test_number_to_words(self):
        random.seed(1)
        numbers = ['1-800-724-6837',
                   '1-617-939-4265',
                   '1-800-228-6277',
                   '953-883-7769']
        self.assertEqual(number_to_words(numbers[0]), '1-800-SAG-6837')
        self.assertEqual(number_to_words(numbers[1]), '1-617-939-HBO-5')
        self.assertEqual(number_to_words(numbers[2]), '1-800-228-OCR-7')
        self.assertEqual(number_to_words(numbers[3]), '953-883-7POX')

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
        numbers = ['1-800-724-6837',
                   '1-617-939-4265',
                   '1-800-228-6277',
                   '953-883-7769']

        words3 = all_wordifications(numbers[2])

        self.assertIn('1-800-PAINT-37', all_wordifications(numbers[0]))
        self.assertEqual(len(all_wordifications(numbers[1])), 15)
        self.assertEqual(len([x for x in words3 if '1-800' in x]),
                         len(words3))


if __name__ == '__main__':
    unittest.main()
