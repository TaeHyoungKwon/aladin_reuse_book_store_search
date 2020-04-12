def encode_euc_kr(search_word):
    return str(search_word.encode("euc-kr")).replace("\\x", "%")[3:-1].upper()
