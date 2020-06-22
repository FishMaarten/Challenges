import re

def score(word:str) -> int:
    if re.match(".*[^A-z].*", word):
        return 0
    return sum([key for char in word.lower() for key in score_dict.keys() if char in score_dict[key]])

score_dict = {
        1: ["a","e","i","o","u","l","n","r","s","t"],
        2: ["d","g"],
        3: ["b","c","m","p"],
        4: ["f","h","v","w","y"],
        5: ["k"],
        8: ["j","x"],
        10:["q","z"] }
