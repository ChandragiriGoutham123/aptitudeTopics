
class someDateGivenToFindSameDay:
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    not_leap_years_in_centuries = [500, 600, 700, 900, 1000, 1100, 1300, 1400, 1500, 1700, 1800, 1900, 2100, 2200, 2300]
    enter_date = int(input("Enter  given date: "))
    enter_month = input("Select one among '1.january' '2.february' '3.march' '4.april''5.may''6.june''7.july''8.august'"
                        "'9.september''10.october''11.november''12.december' as input: ")
    enter_given_year = input("Enter given year : ")
    enter_day_of_given_date: str = input(
        "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
        "'5.friday' '6.saturday': ")
    enter_year = input("Enter year you want to find :")
    if int(enter_year) == int(enter_given_year)+1:
        if int(enter_given_year[len(enter_given_year) - 2:]) % 4 == 0 and int(enter_month) <= 2 and int(
                enter_given_year) not in not_leap_years_in_centuries:
            result_day = int(enter_day_of_given_date) + 2
            result_day = result_day % 7
            print(days[result_day])
        elif int(enter_given_year[len(enter_given_year) - 2:]) % 4 == 0 and int(enter_month) > 2 and int(
                enter_given_year) not in not_leap_years_in_centuries:
            result_day = int(enter_day_of_given_date) + 1
            result_day = result_day % 7
            print(days[result_day])
        elif int(enter_given_year[len(enter_given_year) - 2:]) % 4 != 0 and int(enter_month) <= 2 and int(
                enter_given_year) not in not_leap_years_in_centuries:
            result_day = int(enter_day_of_given_date) + 1
            result_day = result_day % 7
            print(days[result_day])
        elif int(enter_given_year[len(enter_given_year) - 2:]) % 4 != 0 and int(enter_month) > 2 and int(
                enter_given_year) not in not_leap_years_in_centuries:
            result_day = int(enter_day_of_given_date) + 2
            result_day = result_day % 7
            print(days[result_day])
    elif int(enter_year) == int(enter_given_year)-1:
        if int(enter_given_year) % 4 != 0 and int(enter_year) % 4 != 0:
            result_day = int(enter_day_of_given_date) - 1
            if result_day < 0:
                result_day = result_day * (-1)
                results_day = result_day % 7
                print(days[results_day])
            else:
                results_day = result_day % 7
                print(days[results_day])
        elif int(enter_given_year) % 4 != 0 and int(enter_year) % 4 == 0:
            result_day = int(enter_day_of_given_date) - 2
            if result_day < 0:
                result_day = result_day * (-1)
                results_day = 7-result_day
                print(days[results_day])
            else:
                results_day = result_day % 7
                print(days[results_day])
    elif int(enter_year) > int(enter_given_year):
        total_odd_days = 0
        for i in range(int(enter_given_year), int(enter_year)):
            if i not in not_leap_years_in_centuries and i % 4 == 0:
                total_odd_days = total_odd_days + 2
            else:
                total_odd_days = total_odd_days + 1
        total_odd_days = total_odd_days + int(enter_day_of_given_date)
        total_odd_days = total_odd_days % 7
        print(days[total_odd_days])
