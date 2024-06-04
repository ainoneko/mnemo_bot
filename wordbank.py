from collections import defaultdict


class WordBank:
    num_to_chars = ['нл', 'кг', 'бхц', 'тз', 'чр', 'п', 'шщж', 'см', 'вф', 'д']

    char_to_num = {}
    for num in range(10):  # 0..9
        # chars = num_to_chars[num].split()
        chars = list(num_to_chars[num])
        # print ('q', chars)
        for ch in chars:
            char_to_num[ch] = num

    def __init__(self, config=None, wordfile=None):
        self.config = config if config is not None else defaultdict(str)
        self.num_to_words = defaultdict(list)
        if wordfile is not None:
            self.wordfile = wordfile
            self.config['wordfile'] = wordfile
        else:
            # self.wordfile = self.config['wordfile']
            ...

    # @staticmethod
    def word_to_number(self, word: str) -> str:
        # logging.debug('number(%s)', w)
        # print(w)
        num_str = ''
        for ch in word:
            if ch in __class__.char_to_num:
                num_str += str(__class__.char_to_num[ch])

        # logging.debug('number(%s)=%s', w, num_str)
        if num_str != '':
            return num_str  # As string !! Keep the leading zeroes!!
        return None

    def load_words_from_file(self, filename: str = None) -> int:
        # with io.open(WORKFILE, 'r', encoding="utf-8") as f:
        if filename is None:
            filename = self.wordfile
        with open(filename, 'r', encoding="utf-8") as f:
            # read_data = f.readlines()
            found_count = 0
            for word in f.readlines():
                word = word.strip()
                num = self.word_to_number(word)
                # num = __class__.word_to_number(word)

                # logging.debug(word, num)
                # logging.debug(word)
                if num is None:
                    # print(f'FAIL for "{word}"')
                    continue  # No consonants
                # logging.debug(word, num)
                self.num_to_words[num].append(word)
                found_count += 1
            print(word)
        return found_count