import re

def abbreviate(string):
    all_upper = re.findall(r"[A-Z]{2,}", string)
    if len(all_upper) >=1 :
        return all_upper[0]
    
    result = ""
    chopped = re.split(r"[\s|-]", string)
    for word in chopped:
        caps = re.findall(r"[A-Z]", word) 
        if len(caps) > 1:
            for c in caps:
                result += c
        else: result += word[0].upper()
    return result
