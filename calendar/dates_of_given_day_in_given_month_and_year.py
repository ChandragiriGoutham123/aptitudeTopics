class DatesGiven:
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    enter_month = input("Select one among '1.january' '2.february' '3.march' '4.april''5.may''6.june''7.july''8.august'"
                        "'9.september''10.october''11.november''12.december': ")
    number_of_days_in_each_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                                    12: 31}
    enter_day_of_given_date: str = input(
        "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
        "'5.friday' '6.saturday' to find : ")
    enter_year = input("Enter given year: ")
    print("We need to find 1st of given month")
    print("number of odd days in 1600 years is 0")
    print("number of odd days in 400 years is 0")
    print("total odd days in 2000 is '0'")
    total_odd_days = 1
    for i in range(1, int(enter_month)):
        total_odd_days = total_odd_days + number_of_days_in_each_month[i]
    print(total_odd_days)
    total_odd_days = total_odd_days % 7
    print("1st of given month is : " + days[total_odd_days])
    starting_day = 1
    actual_date = 0
    for j in range(1, 7):
        starting_day = starting_day + actual_date
        if j == int(enter_day_of_given_date):
            actual_date = j + 1
            starting_day = starting_day + actual_date

    days_of_given_date = []
    for k in range(5):
        if actual_date <= 31:
            days_of_given_date = days_of_given_date + [actual_date]
        actual_date = actual_date + 7
    for day in days_of_given_date:
        print(str(day) + "th")
