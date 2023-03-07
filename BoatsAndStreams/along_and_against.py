from fractions import Fraction





number_of_inputs = int(input("Enter number of inputs : "))
speeds_boats = []
speeds_stream = []
times = []
distances = []
for i in range(number_of_inputs):
    print("if time is not given place time as 1")
    direction_of_stream_towards_boat = input("enter direction of stream towards 'along and against': ").lower()
    inputs = input(
        "enter to find '1.speed of boat(where downstream time  and upstream time given)' or '2.speeds of streams and boats' or '3.speed of stream(distance different)': ")
    print("Direction of stream : " + direction_of_stream_towards_boat)
    if inputs == "2":
        downstream_distance = input("Enter downstream distance : ")
        print("Downstream distance : " + downstream_distance + " km")
        downstream_time = input("Enter downstream time : ")
        print("Downstream time : " + downstream_time + " hr")
        upstream_distance = input("Enter upstream distance :")
        print("Upstream Distance : " + upstream_distance + " km")
        upstream_time = input("enter upstream time: ")
        print("Upstream time : " + upstream_time + " hr")
        print("downstream speed=downstream distance/downstream time")
        downstream_speed = float(round((Fraction(downstream_distance) / Fraction(downstream_time)), 2))
        print("Downstream speed : " + str(downstream_speed) + " km/hr")
        print("upstream speed=upstream distance/upstream time")
        upstream_speed = float(round((Fraction(upstream_distance) / Fraction(upstream_time)), 2))
        print("Upstream speed : " + str(upstream_speed) + " km/hr")
        speed = input("Enter 'speed of boat' or 'speed of stream' or 'both':").lower()
        if speed == "speed of boat":
            print("Speed of boat=(downstream speed+upstream speed)/2")
            speed_of_boat = float(round((Fraction(downstream_speed) + Fraction(upstream_speed)) / 2, 2))
            if speed_of_boat >= 0:
                speeds_boats = speeds_boats + [speed_of_boat]
                print("Speed of boat : " + str(speed_of_boat) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print("Invalid details")
        elif speed == "speed of stream":
            print("Speed of stream=(downstream speed-upstream speed)/2")
            speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
            if speed_of_stream >= 0:
                speeds_stream = speeds_stream + [speed_of_stream]
                print("Speed of stream : " + str(speed_of_stream) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print("Invalid details")
        elif speed == "both":
            print("Speed of boat=(downstream speed+upstream speed)/2")
            print("Speed of stream=(downstream speed-upstream speed)/2")
            speed_of_boat = float(round((Fraction(downstream_speed) + Fraction(upstream_speed)) / 2, 2))

            if speed_of_boat >= 0:
                speeds_boats = speeds_boats + [speed_of_boat]
                print("Speed of boat : " + str(speed_of_boat) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print("Invalid details")
            speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
            if speed_of_stream >= 0:
                speeds_stream = speeds_stream + [speed_of_stream]
                print("Speed of stream : " + str(speed_of_stream) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print("Invalid details")
    elif inputs == "1":
        downstream_time = Fraction(input("Enter downstream time  (hr): "))
        upstream_time = Fraction(input("Enter upstream time  (hr): "))
        speed_of_stream = Fraction(input("Enter stream speed  (km/hr): "))
        print("Where distance is equal ")
        speed_of_boat = round(
            float((speed_of_stream * (downstream_time + upstream_time)) / (upstream_time - downstream_time)), 2)
        if speed_of_boat >= 0:
            print("Speed of boat (km/hr): " + str(speed_of_boat))
        else:
            print("Enter valid details")
    elif inputs == "3":
        downstream_distance = Fraction(input("Enter downstream distance  (km): "))
        upstream_distance = Fraction(input("Enter upstream distance  (km): "))
        speed_of_boat = Fraction(input("Enter boat speed  (km/hr): "))
        print("Where distance is equal ")
        speed_of_stream = round(float((speed_of_boat * (downstream_distance - upstream_distance)) / (
                    downstream_distance + upstream_distance)), 2)
        if speed_of_boat >= 0:
            print("Speed of boat (km/hr): " + str(speed_of_stream))
        else:
            print("Enter valid details")

if len(distances) > 0:
    total_distances = []
    for long in distances:
        total_distances = total_distances + [str(long) + " Km"]
    total_distances_in_strings = "the distances = "
    for cdistances in total_distances:
        total_distances_in_strings = total_distances_in_strings + "  " + cdistances
    print(total_distances_in_strings)
if len(times) > 0:
    total_times = []
    for hours in times:
        total_times = total_times + [str(hours) + " hr"]
    total_times_in_strings = "the time = "
    for ctimes in total_times:
        total_times_in_strings = total_times_in_strings + "  " + ctimes
    print(total_times_in_strings)
if len(speeds_boats) > 0:
    total_boats = []
    for kmhr in speeds_boats:
        total_boats = total_boats + [str(kmhr) + " Km/hr"]
    total_speeds_boats_in_strings = "the speeds of boats = "
    for cbboats in total_boats:
        total_speeds_boats_in_strings = total_speeds_boats_in_strings + "  " + cbboats
    print(total_speeds_boats_in_strings)
if len(speeds_stream) > 0:
    total_streams = []
    for hrkm in speeds_stream:
        total_streams = total_streams + [str(hrkm) + " Km/hr"]
    total_speeds_streams_in_strings = "the stream speed = "
    for cbstreams in total_streams:
        total_speeds_streams_in_strings = total_speeds_streams_in_strings + " " + cbstreams
    print(total_speeds_streams_in_strings)
find_in_other_distances = input(
    "do you want to find time in other distance in stationary water 'yes' or 'no' : ").lower()
if find_in_other_distances == "yes":
    another_distance = Fraction(input("enter another distance (km/hr): "))
    total_time_in_another_distance = round(float(another_distance / speeds_boats[i - 1]), 2)
    print("Time (hr) : " + str(total_time_in_another_distance))
