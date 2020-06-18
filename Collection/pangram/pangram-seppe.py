import string


# pangram
def is_pangram(text):
    all_letters = list(string.ascii_lowercase)

    if text == '' or text == []:
        return False

    if type(text) == list:
        for element in text:
            return is_pangram(element)

    if type(text) == str:
        for letter in text:
            for alphabet_letter in all_letters:
                if letter == alphabet_letter or letter == alphabet_letter.upper():
                    all_letters.remove(alphabet_letter)

    return all_letters == []
