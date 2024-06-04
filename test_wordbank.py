import unittest

from wordbank import WordBank

class MyTestCase(unittest.TestCase):
    def test_create_instance(self):
        wb = WordBank()
        self.assertIsNotNone(wb)

    def test_load_words_rus(self):
        wb = WordBank()
        self.assertIsNotNone(wb)  # add assertion here


if __name__ == '__main__':
    unittest.main()
