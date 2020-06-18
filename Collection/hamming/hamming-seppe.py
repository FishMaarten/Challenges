class InputError(Exception):
    pass


def distance(strand_one, strand_two):
    hamming_distance = 0
    if type(strand_one) != str or type(strand_two) != str or len(strand_one) != len(strand_two):
        raise InputError("That input doesn't match the requirements: 2 strings of equal length.")

    for i in range(len(strand_one)):
        if strand_one[i] != strand_two[i]:
            hamming_distance += 1

    return hamming_distance
