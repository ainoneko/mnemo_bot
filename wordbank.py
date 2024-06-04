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
        self.config = config if config is not None else {}
        if wordfile is not None:
            self.wordfile = wordfile
            config['wordfile'] = wordfile
        else:
            self.wordfile = config['wordfile']

    def load_words_from_file(self):
        # with io.open(WORKFILE, 'r', encoding="utf-8") as f:
        with open(self.wordfile, 'r', encoding="utf-8") as f:
            read_data = f.readlines()
