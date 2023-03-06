from fractions import Fraction

total_time = Fraction(input("Enter total time (hr): "))
distance = Fraction(input("Enter total distance (km): "))
inputs = input("select one to find between '1.speed of stream' or '2.speed of boat' : ")
if inputs == "1":
    speed_of_boat = Fraction(input("Enter speed of boat (km/hr): "))
    speed_of_stream = ((speed_of_boat**2)-(total_time/(2*distance*speed_of_boat)))**0.5
    speed_of_stream = round(float(speed_of_stream), 2)
    if speed_of_stream >= 0:
        print("speed of stream (km/hr): "+str(speed_of_stream))
    else:
        print("Enter valid details")