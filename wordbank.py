from collections import defaultdict

import logging

logging.basicConfig(level=logging.DEBUG)

ZDF_UTF_TXT = './data/zdf-utf8.txt'

WORD_RUS_TXT = './data/word_rus.txt'


class WordBank:
    num_to_chars = ['нл', 'кг', 'бхц', 'тз', 'чр', 'п', 'шщж', 'см', 'вф', 'д']

    char_to_num = {}
    for num in range(10):  # 0..9
        chars = list(num_to_chars[num])
        for ch in chars:
            char_to_num[ch] = num

    def __init__(self, config=None, wordfile=None):
        self.config = config if config is not None else defaultdict(str)
        self.num_to_words = defaultdict(list)
        self.wordfile = wordfile
        if wordfile is not None:
            self.wordfile = wordfile
            self.config['wordfile'] = wordfile
        else:
            # self.wordfile = self.config['wordfile']
            ...
        if self.wordfile is not None:
            self.load_words_from_file()

    # @staticmethod
    def word_to_number(self, word: str) -> str:
        # logging.debug('number(%s)', w)
        # print(w)
        word = word.lower()
        num_str = ''
        for ch in word:
            if ch in __class__.char_to_num:
                num_str += str(__class__.char_to_num[ch])

        if num_str != '':
            return num_str  # As string ! Keep the leading zeroes!
        return None

    def load_words_from_file(self, filename: str = None) -> int:
        logging.debug(f'load_words_from_file({filename=})')
                
        # with io.open(WORKFILE, 'r', encoding="utf-8") as f:
        if filename is None:
            filename = self.wordfile
        with open(filename, 'r', encoding="utf-8") as f:
            found_count = 0
            for word in f.readlines():
                word = word.strip()
                num = self.word_to_number(word)

                if num is None:
                    continue  # No consonants
                self.num_to_words[num].append(word)
                found_count += 1
            # print(word)
        logging.debug(f'load_words_from_file: {found_count=}, last word: "{word}"')
        return found_count

    def suggest_words_for_num(self, num: str | int, try_split=True, max_count=100):
        logging.debug(f'suggest_words_for_num({num=}, {try_split})')
        # Check if num at all
        if isinstance(num, int):
            num = str(num)
        num = num.strip()
        words = self.num_to_words[num]
        # if strict and words:
        if words or not try_split:
            # max_count ?!
            return words
            
        # Try to split automatically
        # Try to find the longest match
        for tail_start in range(len(num) - 1, 0, -1): # Head can be 1-digit
            logging.debug(f'SPLIT: {tail_start=}, {(num[:tail_start], num[tail_start:])}')
        
            if (head_words := self.suggest_words_for_num(num[:tail_start], try_split=False)):
                tail_words = self.suggest_words_for_num(num[tail_start:])
                logging.debug(f'FOUND FOR SPLIT: {head_words=} {tail_words=}')
                return [head_words, tail_words]
        # Look max len in the dict?
        return words
