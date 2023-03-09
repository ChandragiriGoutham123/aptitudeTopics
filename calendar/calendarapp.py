inputs = input("1.output = to find day for next or before years or after some years\n"
               "2.output = to find same calendar for different years\n""3.output=to find exact day of date\n"
               "4.output = to find day after some days(input=day,after some days)\n""5.output = to find leap year\n"
               "6.output= how many dates the day come in a month\n""7.output= to find 15th of a month\n"
               "8.To find which day not comes last day of century and How many days are in 'x' weeks and 'x' days: ")
if inputs == "1":
    import when_some_date_given_we_want_to_find_same_day_for_another_year
    print(when_some_date_given_we_want_to_find_same_day_for_another_year.someDateGivenToFindSameDay)
elif inputs == "2":
    import same_calendar_for_different_years
    print(same_calendar_for_different_years.sameCalendar)
elif inputs == "3":
    import to_find_exact_day_of_date
    print(to_find_exact_day_of_date.exactDayOfDate)
elif inputs == "4":
    import when_day_given_and_to_find_day_after_some_days
    print(when_day_given_and_to_find_day_after_some_days.toFindDayAfterSomeDays)
elif inputs == "5":
    import to_find_leap_year
    print(to_find_leap_year.toFindLeapYear)
elif inputs == "6":
    import dates_of_given_day_in_given_month_and_year
    print(dates_of_given_day_in_given_month_and_year.DatesGiven)
elif inputs == "7":
    import dates_of_three_sundays_of_even_numbers_is
    print(dates_of_three_sundays_of_even_numbers_is.threeSundays)
elif inputs == "8":
    import other_methods
    print(other_methods.otherMethods)




