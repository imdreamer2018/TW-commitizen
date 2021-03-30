from google_translator import google_translator

commit_message = 'complete case should receive failed and push cost is negative event ' \
                 'when receive given price of positive purchase order cost add price ' \
                 'of remaining stock cost is negative'


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


if __name__ == '__main__':
    author_name = read_author_name_from_config()
    card_name = 'N/A'
    #在这里加上实时控制代码，输入一个英文字符串或者中文字符串时，当我使用空格键时，将输入的字符串传入google_translator方法中，并在下方实时显示correct_message和translate_message
    # message = input()
    correct_message, translate_message = google_translator(commit_message)
    print(correct_message)
    print(translate_message.text)
