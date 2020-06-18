import re

def hey(what):
    # no alphanumerical
    if re.match(r".*\w.*", what) is None:
        return "Fine. Be that way!"
    # refactor whitespace
    what = re.sub(r"\s+", " ", what)
    what = re.sub(r"^\s*|\s*$", "", what)
    # no lowercase 
    if re.match(r".*[a-z\u00e4].*", what) is None:
        if re.match(r".*[A-Z].*", what) is not None:
            return "Whoa, chill out!"
    # ends-with ?
    if re.match(r".+\?$", what) is not None:
        return "Sure."
    return "Whatever."
    words = re.split(r"\s", what)
    print(words)

if __name__ == "__main__":
    while True:
        say = input("Say :")
        print(hey(say))

