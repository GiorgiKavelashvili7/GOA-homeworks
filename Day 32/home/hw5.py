#  Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
#  For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    February = 2
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    elif month >= 10 and month <= 12:
        return 4 