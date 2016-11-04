from __future__  import print_function
#Stair Step Pattern

num_steps = 6

for r in range(num_steps):
    for c in range(r):
        print(' ', end=' ')
    print('#')
#Triangle Pattern
base_size = 8

for r in range(base_size):
    for c in range(r+1):
        print('*', end=' ')
    print()
#Nested loops design

rows = input("Please enter the number of rows: ")
col = input("Please enter the number of columns: ")

for r in range(rows):
    for c in range(col):
        print ('*', end=' ')
    print()


#Test score averages

num_students = input("How many students do you have? ")
num_testscores = input("How many test scores per student? ")

for student in range(num_students):
    total = 0.0
    print('Student number', student + 1, '\n ----------------')
    for test_num in range (num_testscores):
        print('Test number', test_num + 1)
        score = float(input(': '))
        total += score
    average = total/num_testscores
    print('The average for student number', student + 1, 'is: ', average)
    print( )
#Writing an input validation loop
mark_up = 2.5
another = 'y'

while another == 'y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    while wholesale < 0:
        print('ERROR: The cost cannot be negative.')
        wholesale = float(input("Please enter the correct wholesale cost: "))
    retail = wholesale * mark_up

    print('Retail price: $', format(retail, '.2f'))

    another = input("Do you have another item (enter y for yes): ")




#Using a sentinel
tax_factor = 0.0065
print('Enter the property lot number\nor enter 0 to end.')
lot = input("Lot number: ")

while lot != 0:
    value = float(input("Enter the property value: "))
    tax = value*tax_factor

    print('Property tax: $', format(tax, '.2f'))

    print('Enter the next property lot number\nor enter 0 to end.')
    lot = input("Lot number: ")


#Calculating a running total

max = 5
total = 0.0

print('This program calculates the sum of\n', max, 'numbers your will enter.')

for counter in range(max):
    number = input("Enter a number: ")
    total = total + number

print('The total is', total)

#Squares w/ user specified min & max value

print('This program displays a list of numbers\n(starting at 1) and their squares.')
start = input('Enter the starting number: ')
end = input('How high should I go? ')

print('Number\t\tSquare \n------------------')

for number in range(start,end+1):
    square = number**2
    print(number, '\t\t\t', square)



#Squares w/ user specified max value

print('This program displays a list of numbers\n(starting at 1) and their squares.')
end = input('How high should I go? ')

print('Number\t\tSquare \n------------------')

for number in range(1,end+1):
    square = number**2
    print(number, '\t\t\t', square)

#Speed converter

start_speed = 60
end_speed = 131
increment = 10
conversion_factor = 0.6214

print('KPH\t\tMPH\n--------------------')

for kph in range (start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t\t', format(mph, '.1f'))

#Print numbers and their squares

print('Number\t\tSquare \n------------------')

for number in range(1,11):
    square = number**2
    print(number, '\t\t\t', square)

#Using the range function

for x in range(5):
    print('Hello World!')

#Display names

for name in ['Winken', 'Blinken', 'Nod']:
    print (name)

#Display odd numbers in a list

print ('I will display odd numbers 1 through 9.')
for num in [1,3,5,7,9]:
    print (num)

#Display numbers 1-5

print ('I will display numbers 1 through 5.')
for num in [1,2,3,4,5]:
    print (num)
#Temperature check

max_temp = 102.5
temperature = float(input("Enter the substance's Celcius temperature: "))

while temperature > max_temp:
    print('The temperature is too high. \n Turn the temperature down and wait \n 5 minutes. Then take the temperature \n again and enter it.')
    temperature = float(input("Enter the substance's Celcius temperature: "))

print ('The temperature is acceptable. \n Check it again in 15 minutes.')

#Calculating commission
keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input("Enter the commission rate: "))
    commission = sales*comm_rate
    print ("The commission is $", format(commission, ',.2f'))
    keep_going = input("Do you want to calculate another commission (enter y for Yes)? ")