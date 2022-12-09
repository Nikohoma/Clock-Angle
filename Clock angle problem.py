
#                                Clock Angle Problem (Shorter Angle between Hour hand and minute hand)

#                             Name: Nikhil       Section: K22GP       Roll No.: 42         Reg. No.: 12214668



hour=float(input("Hour:"))
min=float(input("Minutes:"))
hour_angle=30*hour + 0.5*min
minute_angle=6*min

diff=abs(hour_angle-minute_angle)

if diff<=180:
    print("Shorter angle between hour hand & minute hand=",diff)
else:
    print("Shorter angle between hour hand and minute hand=",360-diff)

#File operation:
fh=open("test.txt","w")
fh.write("Angle between hour hand and minute hand:\n")
fh.write(str(diff))
fh.write("\n")
fh.write("Shorter angle between hour hand and minute hand:\n")
fh.write(str(360-diff))
fh.close()

