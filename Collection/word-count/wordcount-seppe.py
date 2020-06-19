import re


def word_count(string):
    # empty dictionary to store every occurrence of a word
    count_dict = {}
    # use regex to make a list of all the words in the string, including unicode, but without underscores
    word_list = re.findall("[^\W_]+", string, re.UNICODE)
    # make a key for every word in the dictionary, and set it's value to zero
    for word in word_list:
        count_dict[word.lower()] = 0
    # every time this keyword is encountered, add 1 to it's value
    for word in word_list:
        count_dict[word.lower()] += 1
    return count_dict
