def calc_age(given_date_string):
    import datetime

    current_date = datetime.datetime.now()

    given_date = datetime.datetime.strptime(given_date_string, "%d-%m-%Y")

    # Calculates age based on: day and month comparisons
    if (current_date.month, current_date.day) < (given_date.month, given_date.day):
        age = current_date.year - given_date.year - 1
    else:
        age = current_date.year - given_date.year

    return age


age = calc_age("01-01-1990")
print(age)
