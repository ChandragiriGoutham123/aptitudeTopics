
class sameCalendar:
    given_year = int(input("Enter given year : "))
    total = 0
    for i in range(given_year, given_year + 20):
        if i % 4 != 0:
            total = total + 1

            total = total % 7
            if total % 7 == 0:
                print(i + 1)
                break
        elif i % 4 == 0:
            total = total + 2

            total = total % 7
            if total == 0:
                print(i + 1)
                break
