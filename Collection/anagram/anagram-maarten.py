def detect_anagrams(word:str, candidates:[]) -> []: 
    """ Checks if character_count from candidates matches that of the given word """
    return [w for w in candidates if w.lower() != word.lower()
            and character_count(w) == character_count(word)]

def character_count(word: str) -> {}:
    """ Returns a dictionary with the count of each unique character in word """
    return {c:word.lower().count(c) for c in word.lower()}
