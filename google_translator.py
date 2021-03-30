from googletrans import Translator
from spelling_checker import checker

translator = Translator(service_urls=[
      'translate.google.cn'
    ])


def language_detect(msg):
    language = translator.detect(msg)
    return language.lang


def google_translator(msg):
    if language_detect(msg) == 'en':
        correct_msg = checker(msg)
        return [correct_msg, translator.translate(correct_msg, dest='zh-CN')]
    else:
        return [msg, translator.translate(msg, dest='en')]

