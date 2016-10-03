#1.
x = input("Please enter a value for x: ")
if x > 100:
    y = 20
    z = 40
    print z, y

#2.
a = input("Please enter a value for a: ")
if a < 10:
    b = 0
    c = 1
    print b, c

#3.
a = input("Please enter a value for a: ")
if a < 10:
    b = 0
else:
    b = 99
print b

#4.
A_score = 90
B_score = 80
C_score = 70
D_Score = 60

score = input("Please enter the user's score: ")
if score >= A_score:
    print "Your grade is A."
elif score >= B_score:
    print "Your grade is B."
elif score >= C_score:
    print "Your grade is C."
elif score >= D_Score:
    print "Your grade is D."
else:
    print "Your grade is F."

#5.
amount1 = input("Please enter the first amount: ")
amount2 = input("Please enter the second amount: ")

if amount1 > 10 and amount2 < 100:
    print max(amount1, amount2)

#6.
speed = input("Please input the car's speed: ")
if speed > 24 and speed < 56:
    print "Speed is normal."
else:
    print "Speed is abnormal."

#7.
points = input("Please indicate the point value: ")
if points < 9 or points > 51:
    print "Invalid points."
else:
    print "Valid points."