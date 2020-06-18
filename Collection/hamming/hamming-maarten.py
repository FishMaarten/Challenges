def distance(strand1, strand2):
    count = 0
    for idx, c in enumerate(strand1):
        if strand1[idx] is not strand2[idx]:
            count += 1
    return count
