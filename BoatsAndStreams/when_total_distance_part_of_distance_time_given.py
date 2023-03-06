from fractions import Fraction

total_time = Fraction(input("Enter total time (hr): "))
distance = Fraction(input("Enter total distance (km): "))
first_part_distance = Fraction(input("Enter first part distance (km): "))
second_part_distance = Fraction(input("Enter second part distance (km): "))
inputs = input("select one to find between '1.speed of stream' or '2.speed of boat' : ")
if inputs == "1":
    print("let downstream speed  and upstream speed is equal to 'x'")
    unknown_variable = total_time/((distance/first_part_distance)+(distance/second_part_distance))
    upstream_speed = second_part_distance/unknown_variable
    print("upstream speed (km/hr): "+str(upstream_speed))
    downstream_speed = first_part_distance/unknown_variable
    print("downstream speed (km/hr): "+str(downstream_speed))
    speed_of_stream = (downstream_speed-upstream_speed)/2
    speed_of_stream = round(float(speed_of_stream), 2)
    if speed_of_stream >=0:
      print("speed of stream (km/hr) : "+str(speed_of_stream))
    else:
        print("Enter valid details")
elif inputs == "2":
    print("let downstream speed  and upstream speed is equal to 'x'")
    unknown_variable = total_time/((distance/first_part_distance)+(distance/second_part_distance))
    upstream_speed = first_part_distance/unknown_variable
    print("upstream speed (km/hr): "+str(upstream_speed))
    downstream_speed = second_part_distance/unknown_variable
    print("downstream speed (km/hr): "+str(downstream_speed))
    speed_of_stream = (downstream_speed-upstream_speed)/2
    speed_of_boat = round(float(speed_of_stream), 2)
    if speed_of_stream >= 0:
      print("speed of stream (km/hr) : "+str(speed_of_boat))
    else:
        print("Enter valid details")
