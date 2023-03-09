
class otherMethods:
    inputs = input("1.To find which day not comes last day of century  \n""2.How many days are in 'x' weeks and 'x' days:\n")
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    century_last_days = [2, 4, 6]
    if inputs == "1":
        enter_day_of_given_date_1: str = input(
            "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
            "'5.friday' '6.saturday': ")
        enter_day_of_given_date_2: str = input(
            "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
            "'5.friday' '6.saturday': ")
        enter_day_of_given_date_3: str = input(
            "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
            "'5.friday' '6.saturday': ")
        enter_day_of_given_date_4: str = input(
            "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
            "'5.friday' '6.saturday': ")
        print("Every 100 years have 76 ordinary years and 24 leap years. Odd days in ordinary year = (52 weeks + 1) days."
              " Odd days in a leap year = (52 weeks +2) days. So odd days in 100 years will be (76 x 1 + 24 x 2) "
              "which is 124 odd days.")
        century_years_odd_days = 124 % 7
        two_century_odd_days = (2 * century_years_odd_days) % 7
        three_century_odd_days = (3 * century_years_odd_days) % 7
        four_century_odd_days = (4 * century_years_odd_days) % 7
        if int(enter_day_of_given_date_1) in century_last_days:
            print("last day of century cannot be: "+days[int(enter_day_of_given_date_1)])
        elif int(enter_day_of_given_date_2) in century_last_days:
            print("last day of century cannot be: "+days[int(enter_day_of_given_date_2)])
        elif int(enter_day_of_given_date_3) in century_last_days:
            print("last day of century cannot be: "+days[int(enter_day_of_given_date_3)])
        elif int(enter_day_of_given_date_4) in century_last_days:
           print("last day of century cannot be: "+days[int(enter_day_of_given_date_4)])
    elif inputs == "2":
        number_of_days = input("Enter number of days  as 'x':")
        number_of_weeks = input("Enter number of days  as 'x':")

        print("Total number of days is (7x+x) = 8x")
