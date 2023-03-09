
class toFindDayAfterSomeDays:
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    enter_day_of_given_date: str = input(
        "select given day among '0.sunday' '1.monday' '2.tuesday' '3.wednesday''4.thursday'"
        "'5.friday' '6.saturday': ")
    days_after_actual_day = int(input("Enter after how many days you want to find a day: "))
    actual_day = (int(enter_day_of_given_date) + days_after_actual_day) % 7
    print(days[actual_day])
