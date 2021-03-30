import os
import platform

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
        import curses
        self.stdscr = curses.initscr()
        self.stdscr.keypad(True)
        curses.noecho()

    @staticmethod
    def clear():
        os.system("clear")

    def getkey(self):
        return self.stdscr.getkey()

    def __del__(self):
        import curses
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
BACK_SPACE = b'\x08'

if __name__ == '__main__':
    author_name = read_author_name_from_config()
    card_name = 'N/A'
    # 在这里加上实时控制代码，输入一个英文字符串或者中文字符串时，当我使用空格键时，将输入的字符串传入google_translator方法中，并在下方实时显示correct_message和translate_message
    if platform.system() == "Windows":
        system_handle = WindowsSystemHandle()
    else:
        system_handle = UnixSystemHandle()

    phrase = correct_message = translate_message_text = ''
    system_handle.clear()
    print('Input:\t')
    while True:
        chr = system_handle.getkey()
        byte_chr = chr.encode()
        if byte_chr == ENTER:
            # 如果是换行,则退出循环
            continue
        elif byte_chr == BACK_SPACE:
            # 退格删除
            phrase = phrase[:-1]
        else:
            phrase += chr
        system_handle.clear()
        print('Input:\t', phrase)
        if byte_chr == SPACE:
            correct_message, translate_message = google_translator(phrase)
            translate_message_text = translate_message.text
        print('-' * 20)
        print(correct_message)
        print(translate_message_text)
