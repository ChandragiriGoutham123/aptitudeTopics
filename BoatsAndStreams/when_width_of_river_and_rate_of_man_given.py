from fractions import Fraction


class widthOfRiverRateOfMan:
    rate_of_man = Fraction(input("Enter rate of man (km/hr): "))
    width_of_river = Fraction(input("Enter width of river (km): "))
    time = (width_of_river / rate_of_man) * 60
    time = round(float(time), 2)
    print("time (min): " + str(time))
