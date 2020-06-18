

# takes an int, and returns a bool. If the int is divisible by 4 return True, unless it's divisible by 100, unless it's
# divisible by 400.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
