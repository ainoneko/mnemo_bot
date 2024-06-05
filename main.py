#!/usr/bin/env python3
import telebot
import logging

import wordbank

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    filename='./mnemo_bot_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

import config

ALLOWED_IDS = [335248526]  # ints
cred = config.get_settings()

TOKEN = cred['Token']

MAX_COUNT = 5

bot = telebot.TeleBot(TOKEN)


def extract_arg(arg):
    return arg.split()[1:]


def extract_command(arg):
    return arg.split()[0][1:]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello<b>!</b>', parse_mode='html')


@bot.message_handler(commands=['id'])
def id_(message):
    bot.send_message(message.chat.id, f'Your id is {message.from_user.id}', parse_mode='html')


def get_text(message):
    if len(message.text.split(' ')) < 2:
        # if message.reply_to_message and message.reply_to_message.text:
        #     return message.reply_to_message.text
        #
        # else:
        # return None
        return ''
    else:
        return message.text.split(' ')[1]


@bot.message_handler(commands=['s', 'suggest'])
def suggest(message):
    num = get_text(message)
    # check
    # if num and all(num, lambda x: x.isdigit()):
    if num.isdigit():
        words = wb.suggest_words_for_num(num)
        # bot.send_message(message.chat.id, f'Words for {num}:<br> {words}', parse_mode='html')
        bot.send_message(message.chat.id, f'Words for {num}: {words}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'Expected digits only, but got "{num}"', parse_mode='html')


# if len(message.text.split(' ')) < 2:

# from mailbox import MailBox
# import mailbox
# from status import Status
# from mailbox import MailBox

# @bot.callback_query_handler(func=lambda call: True)
@bot.message_handler(func=lambda message: True)
def callback_all(message):
    for num in (parts := message.text.split(' ')):
        if num.isdigit():
            words = wb.suggest_words_for_num(num)
            bot.send_message(message.chat.id, f'Words for {num}: {words}', parse_mode='html')
        else:
            # Translate word to number
            new_num = wb.word_to_number(num)
            bot.send_message(message.chat.id, f'Number for "{num}": "{new_num}"', parse_mode='html')

    # if len(parts := message.text.split(' ')) < 2:
    #     # return ''
    #     pass
    # else:
    #     num = parts[1]
    # if num.isdigit():
    #     words = wb.suggest_words_for_num(num)
    #     bot.send_message(message.chat.id, f'Words for {num}: {words}', parse_mode='html')
    # else:
    #     # Translate word to number
    #     new_num = wb.word_to_number(num)
    #     bot.send_message(message.chat.id, f'Number for "{num}": "{new_num}"', parse_mode='html')



def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    import wordbank

    global wb
    # wb = wordbank.WordBank(wordfile=wordbank.WORD_RUS_TXT)
    wb = wordbank.WordBank(wordfile=wordbank.ZDF_UTF_TXT)
    main()
