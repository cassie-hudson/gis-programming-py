#7. Color Mixer

color1, color2 = raw_input("Please enter the name of two primary colors, separated by a comma: ")

if color1 == "red" and color2 == "blue":
    print "purple";
elif color1 == "red" and color2 == "yellow":
    print "orange";
elif color1 == "blue" and color2 == "yellow":
    print "Green";
else:
    print "Please enter a primary color."



#1. Day of the Week
weekDay = input("Please choose a number between 1 and 7: ")
if weekDay == 1:
    print "Monday"
elif weekDay == 2:
    print "Tuesday"
elif weekDay == 3:
    print "Wednesday"
elif weekDay == 4:
    print "Thursday"
elif weekDay == 5:
    print "Friday"
elif weekDay == 6:
    print "Saturday"
elif weekDay == 7:
    print "Sunday"
else:
    print "Error!"

#2. Areas of Rectangles
l1, w1 = input("Please enter the length and width of the first rectangle, separated by a comma: ")
l2, w2 = input("Please enter the length and width of the second rectangle, separated by a comma: ")

if (l1*w1) > (l2*w2):
    print "The first rectangle is larger."
else:
    print "The second rectangle is larger."

#3. Age Classifier
age = input("Please enter your age: ")

if age <= 1:
    print "Infant"
elif 1 < age < 13:
    print "Child"
elif 13 <= age < 20:
    print "Teenager"
else:
    print "Adult"

#4. Roman Numerals

number = input("Please enter a number between 1 and 10: ")
if number == 1:
    print "I"
elif number == 2:
    print "II"
elif number == 3:
    print "III"
elif number == 4:
    print "IV"
elif number == 5:
    print "V"
elif number == 6:
    print "VI"
elif number == 7:
    print "VII"
elif number == 8:
    print "VIII"
elif number == 9:
    print "IX"
elif number == 10:
    print "X"
else:
    print "Please enter a number between 1 and 10."

#5. Mass and Weight

mass = input("Please enter the mass of the object: ")
weight = mass * 9.8

if weight > 500:
    print "The object is too heavy."
elif weight < 100:
    print "The object is too light."

#6. Magic Dates

month, day, year = input("Please enter a the month, day and year, separated by a comma: ")

if month * day == year:
    print "That date was magic!"
else:
    print "Better luck next time..."