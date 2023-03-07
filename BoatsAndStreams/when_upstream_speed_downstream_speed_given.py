from fractions import Fraction

upstream_speed = Fraction(input("Enter upstream speed (km/hr): "))
downstream_speed = Fraction(input("Enter downstream speed (km/hr): "))
man_speed = 0.5*(downstream_speed+upstream_speed)
man_speed = round(float(man_speed), 2)
print("man speed (km/hr) :"+str(man_speed))