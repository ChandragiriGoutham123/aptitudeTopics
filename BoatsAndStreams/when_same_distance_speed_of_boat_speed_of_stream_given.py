from fractions import Fraction

speed_of_man = Fraction(input("Enter speed of man with current (Km/hr): "))
speed_current = Fraction(input("enter speed of  current (km/hr) : "))
distance_or_time = input("select one to find  '1.same distance' or '2.time' or '3.half distance' : ").lower()
if distance_or_time == "1":
    distance = Fraction(input("enter distance km : "))

    total_time = round(float((distance/(speed_of_man+speed_current))+(distance)/(speed_of_man-speed_current)), 2)
    if total_time >= 0:
        print("Total time (hr) : "+str(total_time))
    else:
        print("Enter valid details")
elif distance_or_time == "2":
    time = Fraction(input("Enter time (hr) : "))
    downstream_speed = speed_of_man + speed_current
    upstream_speed = speed_of_man - speed_current
    total_distance = round(float((time*downstream_speed*upstream_speed)/(2*speed_of_man)), 2)
    if total_distance >= 0:
        print("Total distance (km) : "+str(total_distance))
    else:
        print("Enter valid details")
elif distance_or_time == "3":
    time = Fraction(input("Enter time (hr) : "))
    downstream_speed = speed_of_man + speed_current
    upstream_speed = speed_of_man - speed_current
    total_distance = round(float((2*time*downstream_speed*upstream_speed)/(3*speed_of_man-speed_current)), 2)
    if total_distance >= 0:
        print("Total distance (km) : "+str(total_distance))
    else:
        print("Enter valid details")