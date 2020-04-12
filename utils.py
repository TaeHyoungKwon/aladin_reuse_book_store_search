import re


def encode_euc_kr(search_word):
    return str(search_word.encode("euc-kr")).replace("\\x", "%")[3:-1].upper()


def is_korean(text):
    return len(re.findall(u"[\u3130-\u318F\uAC00-\uD7A3]+", text)) > 0
