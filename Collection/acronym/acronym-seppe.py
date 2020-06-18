import re


# removeSpecialChars takes a string and returns that string without a defined set of characters that need to be removed.
def removeSpecialChars(sentence):
    # specialChars is a string containing all the characters that you want to remove from the string
    specialChars = ',.:;'
    sentence = sentence.translate({ord(c): None for c in specialChars})  # type: str
    return sentence


# takes a list containing string and returns that list with the string either as itself,
# or as two strings, split at the '-' if it used to contain hyphens
def deHyphen(word_list):
    deHyphened_word_list = []
    for word in word_list:
        deHyphened_word_list += word.split('-')
    return deHyphened_word_list


# splits a string containing a sentence into individual words, returns a list containing those word strings
def splitIntoWords(sentence):
    return sentence.split(' ')


# split words from the list if they contain internal upper case letters, unless every letter in the word is uppercase
# in which case the word remains unchanged.
def SplitInterUpper(word_list):
    new_word_list = []
    for word in word_list:
        # checks if the word is all upper case
        if word != word.upper():
            # splits a word if it contains an internal upper case
            new_word_list += re.findall('.[^A-Z]*', word)
        else:
            new_word_list += [word]
    return new_word_list


# takes a list of strings, and returns a string with the first letter of every string in upper case.
def capitalizeFirst(word_list):
    new_str = ''
    for word in word_list:
        new_str += word[0].upper()
    return new_str


# Main function, takes a string containing multiple words, and returns an abbreviated acronym, following the convention
# as in the test cases.
def abbreviate(long_string):
    # removes the unwanted characters from the string
    long_string = removeSpecialChars(long_string)
    # turn that string into a list of words
    word_list = splitIntoWords(long_string)
    # split words if they contain a hyphen
    word_list = deHyphen(word_list)
    # split words if they contain internal upper case letters
    word_list = SplitInterUpper(word_list)

    acro = capitalizeFirst(word_list)
    print(acro)
    return acro
