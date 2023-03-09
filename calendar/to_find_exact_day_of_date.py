
class exactDayOfDate:
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    no_of_odd_days = {"jan": 0, "feb": 3, "mar": 3, "apr": 6, "may": 1, "jun": 4, "jul": 6, "aug": 2, "sep": 5, "oct": 0,
                      "nov": 3, "dec": 5}
    no_of_odd_days_based_on_input = {"1": 0, "2": 3, "3": 3, "4": 6, "5": 1, "6": 4, "7": 6, "8": 2, "9": 5, "10": 0,
                                     "11": 3, "12": 5}
    not_leap_years_in_centuries = [500, 600, 700, 900, 1000, 1100, 1300, 1400, 1500, 1700, 1800, 1900, 2100, 2200,  2300]
    enter_date = int(input("Enter date you want to find: "))
    enter_month = input("Select one among '1.january' '2.february' '3.march' '4.april''5.may''6.june''7.july''8.august'"
                        "'9.september''10.october''11.november''12.december': ")

    enter_year = input("Enter year you want to find :")
    no_of_odd_days_in_months = 0
    no_of_odd_days_in_years = 0
    checking_for_leap_year = int(enter_year)
    if checking_for_leap_year not in not_leap_years_in_centuries and checking_for_leap_year % 4 == 0:
        no_of_odd_days_in_months = no_of_odd_days_based_on_input[enter_month]
        if 1600 <= int(enter_year) <= 1699:
            no_of_odd_days_in_years = 6
        elif 1700 <= int(enter_year) <= 1799:
            no_of_odd_days_in_years = 4
        elif 1800 <= int(enter_year) <= 1899:
            no_of_odd_days_in_years = 2
        elif 1900 <= int(enter_year) <= 1999:
            no_of_odd_days_in_years = 0
        elif 2000 <= int(enter_year) <= 2099:
            no_of_odd_days_in_years = 6
        step_1 = int(enter_year[len(enter_year)-2:])
        step_2 = int(step_1/4)
        step_3 = enter_date
        step_4 = no_of_odd_days_in_months
        step_5 = no_of_odd_days_in_years
        final_step = (step_1+step_2+step_3+step_4+step_5) % 7
        if final_step == 0 and int(enter_month) <= 2:
            print(days[7])

        if int(enter_month) <= 2:
            print(days[final_step-1])


        else:
            print(days[final_step])

    else:
        no_of_odd_days_in_months = no_of_odd_days_based_on_input[enter_month]
        if 1600 <= int(enter_year) <= 1699:
            no_of_odd_days_in_years = 6
        elif 1700 <= int(enter_year) <= 1799:
            no_of_odd_days_in_years = 4
        elif 1800 <= int(enter_year) <= 1899:
            no_of_odd_days_in_years = 2
        elif 1900 <= int(enter_year) <= 1999:
            no_of_odd_days_in_years = 0
        elif 2000 <= int(enter_year) <= 2099:
            no_of_odd_days_in_years = 6
        step_1 = int(enter_year[len(enter_year) - 2:])
        step_2 = int(step_1 / 4)
        step_3 = enter_date
        step_4 = no_of_odd_days_in_months
        step_5 = no_of_odd_days_in_years
        final_step = (step_1 + step_2 + step_3 + step_4 + step_5) % 7
        print(days[final_step])





