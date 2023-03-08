from fractions import Fraction


class distanceAverageSpeedAndTime:
    down_stream_distance = Fraction(input("Enter downstream distance (miles): "))
    average_speed_downstream = Fraction(input("Enter average speed downstream (miles/hr): "))
    time_while_going_upstream_in_hours = Fraction(input("Enter time while going upstream (hr): "))
    print("Give minutes/60 as input")
    time_while_going_upstream_in_minutes = Fraction(input("Enter time while going upstream (minutes): "))
    time = time_while_going_upstream_in_minutes + time_while_going_upstream_in_hours
    time_taken_to_cover_downstream = down_stream_distance / average_speed_downstream
    total_time = time + time_taken_to_cover_downstream
    print("average speed= average distance /time")
    average_speed = round(float((2 * down_stream_distance) / total_time), 2)
    if average_speed >= 0:
        print("Average speed (miles/hr): " + str(average_speed))
    else:
        print("Enter valid details")
