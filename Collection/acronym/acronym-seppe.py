import re


def splitIntWords(sentence):
    return sentence.split(' ')


def remSpecialChars(sentence):
    specialChars = ',.:;'
    sentence = sentence.translate({ord(c): None for c in specialChars})  # type: str
    return sentence


def deHyphen(word):
    return word.split('-')


def abbreviate(long_string):
    acro = ''
    long_string = remSpecialChars(long_string)
    hword_list = splitIntWords(long_string)
    word_list = []
    for word in hword_list:
        word_list += deHyphen(word)
    new_word_list = []
    for word in word_list:
        if word != word.upper():
            new_word_list += re.findall('.[^A-Z]*', word)
        else:
            new_word_list += [word]
    for word in new_word_list:
        acro += word[0]
    result = acro.upper()
    print(result)
    return result
