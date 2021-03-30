import curses
import os
import platform
import time
from threading import Thread

from google_translator import google_translator

commit_message = 'complete case should receive failed and push cost is negative event ' \
                 'when receive given price of positive purchase order cost add price ' \
                 'of remaining stock cost is negative'


class WindowsSystemHandle(object):
    def getkey(self):
        import msvcrt
        return msvcrt.getch().decode()

    @staticmethod
    def clear():
        os.system("cls")


class UnixSystemHandle(object):
    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.keypad(True)
        curses.noecho()

    @staticmethod
    def clear():
        os.system("clear")

    def getkey(self):
        return self.stdscr.getkey()

    def __del__(self):
        curses.endwin()


def read_author_name_from_config():
    with open('./config.txt', 'r') as f:
        name = f.readlines()[0].split('=')[1]
        return name


def setting_author_name(name):
    with open('./config.txt', 'r') as f1:
        content = f1.readlines()
    content[0] = 'default_author_name={}\n'.format(name)
    with open('./config.txt', 'w') as f2:
        f2.writelines(content)


ENTER = b'\n'
SPACE = b' '
BACK_SPACE = b'\x7f'


class Params(object):
    phrase = ''
    correct_message = ''
    translate_message_text = ''
    stop = False


def show_content():
    system_handle.clear()
    print('\rInput:\t', params.phrase)
    print('\r', '-' * 100)
    print('\r', params.correct_message)
    print('\r', params.translate_message_text)


def translation_run():
    intermediate_phrase = ''
    while not params.stop:
        space_index = params.phrase.rfind(' ')  # 去除掉末尾单词
        phrase = params.phrase[:space_index]
        if phrase != intermediate_phrase:
            # 本次输入与上次不一样 须要识别
            params.correct_message, translate_message = google_translator(params.phrase)
            params.translate_message_text = translate_message.text
            show_content()
        time.sleep(1)


if __name__ == '__main__':
    params = Params()
    author_name = read_author_name_from_config()
    card_name = 'N/A'
    # 在这里加上实时控制代码，输入一个英文字符串或者中文字符串时，当我使用空格键时，将输入的字符串传入google_translator方法中，并在下方实时显示correct_message和translate_message
    if platform.system() == "Windows":
        system_handle = WindowsSystemHandle()
    else:
        system_handle = UnixSystemHandle()

    system_handle.clear()
    Thread(target=translation_run).start()
    print('Input:\t')
    while True:
        chr = system_handle.getkey()
        byte_chr = chr.encode()
        if byte_chr == ENTER:
            # 如果是换行,则退出循环
            chr = ''
            params.stop = True
            break
        elif byte_chr == BACK_SPACE:
            # 退格删除
            params.phrase = params.phrase[:-1]
        else:
            params.phrase += chr

        show_content()
