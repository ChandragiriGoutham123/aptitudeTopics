from fractions import Fraction

speed_of_man = Fraction(input("Enter speed of man with current (Km/hr): "))
speed_of_man_against_current = Fraction(input("enter speed of man against current (km/hr) : "))

rate = input("You want to find 'against' or 'along' speed : ").lower()
if rate == "against":
    against_speed = round(float((2*speed_of_man)+speed_of_man_against_current), 2)
    if against_speed >= 0:
      print("Against speed (km/hr) : "+str(against_speed))
    else:
        print("Enter valid details")
elif rate == "along":
    along_speed = round(float((2*speed_of_man)-speed_of_man_against_current), 2)
    if along_speed >= 0:
       print("Against speed (km/hr) : " + str(along_speed))
    else:
        print("Enter valid details")

