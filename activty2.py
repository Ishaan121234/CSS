city = input("Enter yor city name")
temp = float(input("Enter Today's temperature in C: "))

print("City:", city)
print("Temperature:", temp)

if temp > 35:
    print("Warning: it is very hot today!!")
if temp > 25:
        print("Great Day to go outside!!")
else:
      print("Grab a jacket before you go outside")

if temp > 35:
      print("Weather: Scorching Hot")
elif temp > 25:
      print("Weather: Warm and Sunny")
elif temp > 15:
      print("Weather: Cool and Breezy")
else: 
      print("Weather: Cold -- stay warm!!")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))