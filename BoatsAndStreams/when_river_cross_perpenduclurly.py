from fractions import Fraction


class riverCrossPerpendicularly:
    time_of_man_normal_river = Fraction(input("Time of man on normal river (min): "))
    time_of_man_flowing_river = Fraction(input("Time of man on flowing river (min): "))
    width_of_river = Fraction(input("Velocity of river (meters): "))
    velocity_of_river = (width_of_river*((1/time_of_man_normal_river**2)-(1/time_of_man_flowing_river**2))**0.5)
    velocity_of_river = round(float(velocity_of_river), 2)
    print("Velocity of river (m/min): "+str(velocity_of_river))