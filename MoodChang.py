
name = input("Enter your name: ")
mood = input("How are you feeling today? happy/sad/tired/great/unhappy: ")
energy = int(input("Enter your energy level from 1 to 15: "))


if energy < 3:
    print("Alert: Your energy seems low today. Please take some rest for your body.")


if energy >= 5:
    print("You have enough energy to do something productive today!")
else:
    print("Take it slow today and do something relaxing.")

if mood == "happy":
    advice = "Keep spreading your positive energy!"
elif mood == "sad":
    advice = "Talk to someone you trust or do something that makes you feel better."
elif mood == "tired":
    advice = "Drink water, take a short break, and rest your mind."
elif mood == "stressed":
    advice = "Try deep breathing or make a small to-do list."
elif mood == "excited":
    advice = "Use your excitement to start something creative!"
else:
    advice = "Every mood is okay. Take care of yourself today."

import datetime

today = datetime.datetime.now()


print("\n================================")
print("DAILY MOOD ADVISOR REPORT")
print("================================")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("================================")
