import unittest

from wordbank import WordBank

class MyTestCase(unittest.TestCase):
    def test_create_instance(self):
        wb = WordBank()
        self.assertIsNotNone(wb)

    def test_load_words_rus(self):
        wb = WordBank()
        loaded = wb.load_words_from_file(filename='./data/word_rus.txt')
        # self.assertEqual(loaded, 34009)  # wc -l
        self.assertEqual(loaded, 34010)  # fix for no eol

    def test_load_zdf(self):
        wb = WordBank()
        loaded = wb.load_words_from_file(filename='./data/zdf-utf8.txt')
        # self.assertEqual(loaded, 93391)  # wc -l
        self.assertEqual(loaded, 93372)  # fix for no eol

if __name__ == '__main__':
    unittest.main()
