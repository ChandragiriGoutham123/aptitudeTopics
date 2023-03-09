
class toFindLeapYear:
    not_leap_years_in_centuries = [500, 600, 700, 900, 1000, 1100, 1300, 1400, 1500, 1700, 1800, 1900, 2100, 2200,  2300]
    input_years = list(map(int, input("Enter years in space given format : ").split()))
    leap_year = 0
    for years in input_years:
        if years in not_leap_years_in_centuries and years % 4 == 0:
            leap_year = years
    print(leap_year)
