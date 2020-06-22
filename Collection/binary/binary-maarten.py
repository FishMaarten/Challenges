import re

def parse_binary(binary:str) -> int:
    if re.match(r".*[A-z2-9].*", binary):
        raise(ValueError("This is not a binary string"))

    series = [2**i for i in range(32)][len(binary)::-1][::-1]
    
    result = 0
    for idx, b in enumerate(binary[::-1]):
        result += int(b) * series[idx] 
    return result 
