from fractions import Fraction


class manSpeedWithCurrentAndCurrentSpeed:
    speed_of_man_with_current = Fraction(input("Enter speed of man with current (Km/hr): "))
    speed_of_current = Fraction(input("enter speed of current (km/hr) : "))
    mans_rate_in_still_water = round(float(speed_of_man_with_current - speed_of_current), 2)
    rate = input("You want to find 'against' or 'along' speed : ").lower()
    if rate == "against":
        against_speed = round(float(mans_rate_in_still_water - speed_of_current), 2)
        if against_speed >= 0:
            print("Against speed (km/hr) : " + str(against_speed))

        else:
            print("Enter valid details")

    elif rate == "along":
        along_speed = round(float(mans_rate_in_still_water + speed_of_current), 2)
        if along_speed >= 0:
           print("Against speed (km/hr) : " + str(along_speed))
        else:
            print("Enter valid details")
