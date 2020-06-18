def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # populate alphabet dictionary with zeros
    alpha_count = {}
    for c in alphabet:
        alpha_count[c] = 0
    # increment dict value for each char in sentence
    for c in sentence:
        if c.lower() in alpha_count.keys():
            alpha_count[c.lower()] += 1
    # check if every letter is at least 1
    if all(alpha_count.values()):
        return True
    return False
