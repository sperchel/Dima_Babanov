# Den has invited some friends. His list is:
#
# s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
#
# Could you make a program that
# · makes this string uppercase
# · gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result
# between parentheses separated by a comma.
# So the result of function meeting(s) will be:
# Examples:
#
# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL,
# BJON)"
#
#
# It can happen that in two distinct families with the same family name two people have the same first name too.


def meeting(s):
    return ''.join(sorted(['(' + i.split(':')[1].upper() + ', ' + i.split(':')[0].upper() + ')' for i in s.split(';')]))


if __name__ == '__main__':
    print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;"
                  "Lewis:Kern;Megan:Stan;Alex:Korn"))  # (ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN,
    # LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)
    print(meeting("John:Gates;Michael:Wahl;Megan:Bell;George:Gates;Stan:Wahl;Alex:Meta;Ann:Gates;Alex:Korn"))  # (BELL,
    # MEGAN)(GATES, ANN)(GATES, GEORGE)(GATES, JOHN)(KORN, ALEX)(META, ALEX)(WAHL, MICHAEL)(WAHL, STAN)
    print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;"
                  "Lewis:Kern;Megan:Stan;Alex:Korn"))  # (ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN,
    # LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)
    print(meeting("John:Gates;Michael:Wahl;Megan:Bell;George:Gates;Stan:Wahl;Alex:Meta;Ann:Gates;Alex:Korn"))  # (BELL,
    # MEGAN)(GATES, ANN)(GATES, GEORGE)(GATES, JOHN)(KORN, ALEX)(META, ALEX)(WAHL, MICHAEL)(WAHL, STAN)
