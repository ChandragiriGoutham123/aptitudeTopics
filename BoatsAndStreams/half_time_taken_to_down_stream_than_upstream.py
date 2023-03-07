from fractions import Fraction

upstream_speed = Fraction(input("Enter upstream speed as 1 (km/hr): "))
downstream_speed = Fraction(input("Enter downstream speed 2 (km/hr): "))
man_speed = (downstream_speed+upstream_speed)
stream_speed = (downstream_speed-upstream_speed)

print("ratio :"+str(man_speed)+":"+str(stream_speed))