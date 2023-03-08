from fractions import Fraction


class upstreamDistanceDownstreamDistance:
    upstream_distance_one = Fraction(input("Enter upstream distance (km): "))
    downstream_distance_one = Fraction(input("Enter downstream distance (km) : "))
    upstream_distance_two = Fraction(input("Enter second upstream distance (km): "))
    downstream_distance_two = Fraction(input("Enter second downstream distance (km) : "))
    time_one = Fraction(input("Enter total time (hr): "))
    time_two = Fraction(input("Enter total second time (hr): "))
    print("We can find both speed of stream and boat with help of these")
    values = []
    for i in range(1, 100):
        for j in range(1, 100):
            if ((upstream_distance_one/i)+(downstream_distance_one/j)) == time_one and \
                    ((upstream_distance_two/i)+(downstream_distance_two/j)) == time_two:

                values = values + [i]
                values = values + [j]
                break
    print(values)
    downstream_speed = values[1]
    upstream_speed = values[0]
    speed_of_stream = round(float((downstream_speed-upstream_speed)/2), 2)
    speed_of_boat = round(float((downstream_speed+upstream_speed)/2), 2)
    inputs = input("Select one to find '1.speed of stream' '2.speed of boat': ")
    if inputs == "1":
        print("speed of stream (km/hr): "+str(speed_of_stream))
    elif inputs == "2":
        print("speed of boat (km/hr): "+str(speed_of_boat))
