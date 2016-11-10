from __future__ import print_function
#14. Pound Pattern
base_size = 7

for r in range (base_size):
    print("#",end='')
    for c in range(r+1):
        print(' ', end='')
    print("#")


#13 Star Pattern
base_size = 7

for r in range(base_size, 1, -1):
    for c in range(r-1):
        print("*",end="")
    print()



#12. Population
int = input("What is the initial number of organisms? ")
rate = input("What is the average daily increase of these organisms? ")
days = input("How many days does the organism have to multiply? ")
print ("Day Approximate\t\tPopulation")
for x in range (1, days +1):
    population = (int * rate)*x + int
    print(x,"\t\t\t\t\t", population)


#11. Calculating the Factorial of a Number

number = input("Please enter a number: ")
factorial = 1

for x in range(1, number + 1):
    factorial = factorial * x
print (factorial)

#10. Tuition Increase
tuition = 8000



for y in range (1, 6):
    tuition = tuition + tuition*0.03
    print(format(tuition, '.2f'))
#9. Ocean Levels

for y in range(1, 26):
    rise = 1.6 * y
    print (y, rise)
#8. Sum of Numbers
number = input("Please enter a positive number to start the program. Enter a negative number to stop computing. ")
total = 0
while number > 0:
    number = input("Please enter a positive number to start the program. Enter a negative number to stop computing. ")
    total = number + total
print(total)

#7. Pennies for Pay

days = input("How many days have you worked? ")
total = 0
print("Daily Earnings:")
print("----------------")
for d in range(1, days + 1):
    pay = 2**d
    print(pay)
    total = total + pay
print("\nTotal: $",format(float(total)/100, '.2f'), sep="")

#6. Celcius to Farenheit Table


print ("Celcius\tFarenheit")
print ("------------------")
for cel in range (0,21):
    farenheit = cel*(9/5)+32
    print (cel, "\t\t", farenheit)


#5. Average Rainfall

total = 0
years = input("For how many years should we calculate rainfall? ")

for y in range (1, years +1):
    for m in range (0, 12):
        rainfall = input("How many inches of rain fell in this month? ")
        total = rainfall + total
    months = years * 12
print(months)
print(total)
avg = total/months
print(avg)

#4. Distance Traveled
speed = input("How fast is the vehicle traveling? ")
hours = input("How long has the vehicle been traveling? ")

for x in range(1, hours + 1):
    x = speed * x
    print(x)

#3. Budget Analysis

budget = input("How much have you budgeted for this month? ")
total = 0
keep_going = "y"

while keep_going == "y":
    expense = input("Enter your next expense: ")
    total = total + expense
    keep_going = raw_input("Do you have another expense? ")
if total > budget:
    print("You are overbudget by", budget-total,"dollars.")
else:
    print("You are within the budget.")


#2. Calories Burned

for cal in range(10, 31, 5):
    cal_burn = cal * 4.2
    print(cal_burn)


#1. Bug Collector

total = 0


for d in range(0,5):
    bugs = input("How many bugs did you collect? ")
    total = bugs + total
print(total)