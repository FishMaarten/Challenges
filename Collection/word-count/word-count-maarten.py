import re
def word_count(sentence):
    word_dict = {}
    # add or increment stripped words 
    for word in re.findall(r"[^\W_]+", sentence):
        if word.lower() not in word_dict.keys():
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1
    return word_dict
