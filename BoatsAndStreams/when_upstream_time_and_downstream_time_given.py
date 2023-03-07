from fractions import Fraction
inputs = input("please select one '1.time between two points' or '2.time between three points' :")
if inputs == "1":
    time_while_going_upstream_in_hours = Fraction(input("Enter time while going upstream (hr): "))
    print("Give minutes/60 as input")
    time_while_going_upstream_in_minutes = Fraction(input("Enter time while going upstream (minutes): "))
    time_upstream = time_while_going_upstream_in_minutes + time_while_going_upstream_in_hours
    time_while_going_downstream_in_hours = Fraction(input("Enter time while going downstream (hr): "))
    print("Give minutes/60 as input")
    time_while_going_downstream_in_minutes = Fraction(input("Enter time while going downstream (minutes): "))
    time_downstream = time_while_going_downstream_in_minutes + time_while_going_downstream_in_hours
    ratio_of_speed_of_boat_speed_of_current = Fraction((time_downstream+time_upstream)/(time_upstream-time_downstream))
    print("ratio : "+str(ratio_of_speed_of_boat_speed_of_current))
elif inputs == "2":
    time_while_going_and_comeback_hours = Fraction(input("Enter time while going and comeback (hr): "))
    print("Give minutes/60 as input")
    time_while_going_and_comeback_minutes = Fraction(input("Enter time while going and comeback (minutes): "))
    time_while_going_and_comeback = time_while_going_and_comeback_hours + time_while_going_and_comeback_minutes
    time_while_going_in_hours = Fraction(input("Enter time while going  (hr): "))
    print("Give minutes/60 as input")
    time_while_going_in_minutes = Fraction(input("Enter time while going  (minutes): "))
    time_while_going = time_while_going_in_hours + time_while_going_in_minutes
    ratio_of_speed_of_boat_speed_of_current = Fraction(
        (time_while_going_and_comeback) / (time_while_going_and_comeback-time_while_going))
    print("ratio : " + str(ratio_of_speed_of_boat_speed_of_current))
