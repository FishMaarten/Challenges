def is_leap_year (year):
    if year %4 is 0:
        if year %100 is 0:
            if year %400 is 0:
                return True
            return False
        return True
    return False
