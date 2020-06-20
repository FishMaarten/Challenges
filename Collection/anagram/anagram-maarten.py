def detect_anagrams(word:str, candidates:[]) -> []: 
    """ Checks if char_count from candidates matches that of the given word """
    return [w for w in candidates if w.lower() != word.lower() and character_count(w.lower()) == character_count(word.lower())]

def character_count(word: str) -> {}:
    """ Returns a dictionary with the count of each unique character in word """
    return {c:word.count(c) for c in word}

print(detect_anagrams("banana", ["sgdfs", "abnana", "banana"]))
