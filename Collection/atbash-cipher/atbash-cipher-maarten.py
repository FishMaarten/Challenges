import re
from string import ascii_lowercase as ALPHA 

alpha = {k:ALPHA[len(ALPHA)-idx-1] for idx, k in enumerate(ALPHA)}
for i in range(10):
    alpha[str(i)] = str(i)

def encode(sentence:str) -> str:
    sentence = re.sub("\W", "", sentence)
    result = ""
    for idx, c in enumerate("".join(alpha[c] for c in sentence.lower())):
        if idx is not 0 and idx % 5 is 0:
            result += " "
        result += c 
    return result
    
def decode(cypher:str) -> str:
    cypher = re.sub("\W","", cypher)
    return "".join(alpha[c] for c in cypher.lower())
