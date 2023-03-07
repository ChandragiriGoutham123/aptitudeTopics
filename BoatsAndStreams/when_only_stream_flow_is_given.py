from fractions import Fraction

upstream_speed = Fraction(input("Enter upstream speed as 1 (km/hr): "))
downstream_speed = Fraction(input("Enter downstream speed 2 (km/hr): "))

upstream_speed = 3 * upstream_speed
downstream_speed = 3 * downstream_speed
speed_of_boat = 0.5*(upstream_speed+downstream_speed)
print("Speed of boat (km/hr): "+str(speed_of_boat))
