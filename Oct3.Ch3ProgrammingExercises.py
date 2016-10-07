#12. Software Sales
packages = input("How many packages would you like to purchase?: ")
cost = 99

if packages > 100:
    amt = cost*.6
elif 50 <= packages < 100:
    amt = cost*.7
elif 20 <= packages < 50:
    amt = cost*.8
elif 10 <= packages <20:
    amt = cost*.9
else:
    amt = 99
print "The total amount of your purchase is $" +str((amt*packages, f))+"."

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

#7. Color Mixer

color1, color2 = raw_input("Please enter the name of two primary colors: ").split()

if color1 == "red" and color2 == "blue":
    print "purple";
elif color1 == "red" and color2 == "yellow":
    print "orange";
elif color1 == "blue" and color2 == "yellow":
    print "Green";
else:
    print "Please enter a primary color."

#8. Hotdog Cookout Calculator
guests = input("How many guests will attend the cookout?: ")
hotdogs = input("How many hotdogs will each guest be given?: ")
total = guests*hotdogs
weenies = (total)/10
print "We will need", weenies, "packages of weenies."
print "There will be", total%10, "weenies leftover."
buns = (total)/8
print "We will need", buns, "packages of buns."
print "There will be", total%8, "buns left over."

#9. Roulette Wheel Colors
pocket = input("Please enter your pocket number: ")

if pocket == 0:
    print "Green"
elif pocket < 11 or (19 < pocket < 28):
    if pocket % 2==0:
        print "Black";
    else:
        print "Red";
elif (11 <= pocket <= 19) or (29 <= pocket <= 36):
    if pocket % 2 == 0:
        print "Red";
    else:
        print "Black"
else:
    print "Please choose a valid number."

#10. Money Counting Game
quarter = input("How many quarters would you like to add?: ")
nickel = input("How many nickels would you like to add?: ")
penny = input("How many pennies would you like to add?: ")
dime = input("How many dimes would you like to add?: ")

amt = (quarter*25) + (nickel*5) + (penny*1) + (dime*10)

if amt == 100:
    print "Congratulations! You won the game!"
elif amt < 100:
    print "Sorry, but the amount you entered was less than $1.00."
else:
    print "Sorry, but the amount you entered was greater than $1.00."

#11. Book Club Points
books = input("How many books have you purchased this month?: ")

if books > 8:
    print "You earned 60 points!"
elif books >= 6:
    print "You earned 30 points!"
elif books >=4:
    "You earned 15 points!"
elif books >= 2:
    "You earned 5 points!"
elif books < 2:
    "You have 0 points..."