import unittest

import logging

from wordbank import WordBank

logging.basicConfig(level=logging.DEBUG)


# logging.basicConfig(level=logging.INFO)

ZDF_UTF_TXT = './data/zdf-utf8.txt'

WORD_RUS_TXT = './data/word_rus.txt'


class MyTestCase(unittest.TestCase):
    def test_create_instance(self):
        wb = WordBank()
        self.assertIsNotNone(wb)

    def test_suggest_splitted(self):
        wb =  WordBank(wordfile=WORD_RUS_TXT)
        sugg = wb.suggest_words_for_num('111222')
        print(sugg)
        print('-----------')
        sugg = wb.suggest_words_for_num('111222333')
        print(sugg)
        # self.assertEqual(sugg1, sugg2)
        # self.assertEqual(['акциз'], sugg2)
        # exit()

    def test_load_words_rus(self):
        wb = WordBank()
        loaded = wb.load_words_from_file(filename=WORD_RUS_TXT)
        # self.assertEqual(loaded, 34009)  # wc -l
        self.assertEqual(loaded, 34010)  # fix for no eol
        self.assertEqual(len(wb.num_to_words), 21492)  # fix for no eol

    def test_load_zdf(self):
        wb = WordBank()
        loaded = wb.load_words_from_file(filename=ZDF_UTF_TXT)
        # self.assertEqual(loaded, 93391)  # wc -l
        self.assertEqual(loaded, 93372)  # fix for no eol

    def test_absatz(self):
        wb1 = WordBank(wordfile=WORD_RUS_TXT)
        self.assertEqual(wb1.word_to_number('абзац'), '232')

        wb2 = WordBank(wordfile=ZDF_UTF_TXT)
        self.assertEqual(wb2.word_to_number('абзац'), '232')

    def test_suggest_for_123(self):
        wb1 = WordBank(wordfile=WORD_RUS_TXT)
        # wb1 = WordBank(wordfile=ZDF_UTF_TXT)
        sugg1 = wb1.suggest_words_for_num('123')
        # sugg1 = wb1.suggest_words_for_num('1')
        # sugg1 = wb1.suggest_words_for_num('232')
        sugg2 = wb1.suggest_words_for_num(123)
        print(sugg1)
        self.assertEqual(sugg1, sugg2)
        self.assertEqual(['акциз'], sugg2)
        # ZDF: ['акциз', 'губить', 'кобза', 'огибать']


if __name__ == '__main__':
    unittest.main()
