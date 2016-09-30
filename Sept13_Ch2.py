#Algorithm workbench
#1. Height
height = input("Please enter your height in inches: ")
print str(height), 'inches'

#2. Favorite color
color = raw_input("Please enter your favorite color: ")
print color

#3. Assignment Statements
a=0
b=0

b = a + 2
print b
a = b*4
print a
b=a/3.14
print b
a=b-8
print a

#4. What are the results?
w = 5
x = 4
y = 8
z = 2

result = x + y
print result
result = z * 2
print result
result = y/x
print result
result = y - z
print result
result = w//z
print result

#5.
total = 10 + 14
print total

#6.
down_payment = input("Please enter your down payment: ")
due = total - down_payment

#7.
subtotal = input('Please enter the subtotal: ')
total = subtotal * 0.15

#8.
a = 5
b = 2
c = 3

result = a+b+c
print(result)

#9.

num = 99
num = 5
print(num)

#10.
sales = format(100000.2135148, '.2f')
print sales

#11.
number = format(1234567.456, ',.1f')

#12.
print('George', 'John', 'Paul', 'Ringo')



#Formatting integers
print(format(12345, 'd'))
print(format(12345, ',d'))
print(format(12345, '10d')) #10 spaces wide

#Specifying a minimum field width (useful for printing numbers of different lengths in columns)

num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999


print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))

#Formatting float point numbers as a percentage
print(format(0.5, '%'))
print(format(0.5, '.0%'))

monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print 'Your annual pay is $', \
    format(annual_pay, ',.2f')

#Displaying floating point numbers
amount_due = 5000.0
monthly_payment = amount_due/12
print'The monthly payment is', monthly_payment
#Use the format function to change the number of decimal places
print'The monthly payment is', format(monthly_payment, '.2f')
#Use the format function to display in scientific notation
print'The monthly payment is', format(monthly_payment, 'e')
print'The monthly payment is', format(monthly_payment, '.2e')

#Use the format function to insert comma separators
print'The monthly payment is', format(1234567.9875, ',.2f')

#String concatenation

print('This is ' + 'one string.')

print('Enter the amount of ' +\
      'sales for each day and '+\
    'press Enter.')


#Prints on a new line, \t adds a tab

print'One\nTwo\nThree'

print('Mon\tTues\tThurs')


#Converting a math problem to a programming statement
#Get the desired future value, current interest rate, number of years the money will sit in the account.

future_value = float(input('What is the amount of money you would like to save? '))
interest_rate = float(input('What is the interest rate on this account? '))
years = input('How many years will the money remain in the account? ')

present_value = future_value/(1.0+interest_rate)**years

print 'This is the amount of the deposit: ', present_value

#The remainder operator--creating a time converter program
#Get the number of seconds from the user.
total_seconds = float(input('Enter the number of seconds: '))
#Get the number of hours
hours = total_seconds//60
#Get the total number of minutes
minutes = (total_seconds//60)%60
#Get the remaining seconds
seconds = total_seconds % 60

#Display results.
print 'Here is the time in hours, minutes, and seconds: '
print 'Hours: ', hours
print 'Minutes: ', minutes
print 'Seconds', seconds


#Program to calculate an average
#Get the test scores
test1 = float(input("Enter the first test score: "))
test2 = float(input("Enter the second test score: "))
test3 = float(input("Enter the third test score: "))

#Calculate the average of the three scores
average = (test1 + test2 + test3)/3.0

#Display the average
print 'Your average is: ', average

#Program to calculate a percentage
#Prompt user to enter original price
original_price = float(input("Enter the item's original price: "))
#Multiply the original price by the percentage off
discount = original_price * 0.2
#Calculate the sales price
sale_price = original_price - discount
#Print new price
print 'The sale price is:', sale_price


#print function; to enclose string literals, you can use either single or double-quotes; triple quoted strings can contain both single and double quotes within; can also be used for multi-line arguments

print('Hello World!')
print('Cassie Hudson')
print ('3300 Fallmeadow St')
print ('Denton, TX 76207')
print("""I'm reading "Hamlet" tonight.""")
print("""one
two
three""")

#Variables
age = 25 #Create the variable age and have it reference the value 25
width = 10
length = 5
print(width) #When you pass a variable as an argument to the print function, you do not enclose the variable name in quote marks.
print(length)

#This program demonstrates a variable
room = 503
print('I am staying in room number')
print(room)

#Create two variables: top_speed and distance.
top_speed = 160
distance = 300

#Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print("The distance traveled is")
print(distance)

#Displaying multiple items with the print function
print'I am staying in room number' ,room

#Variable reassignment
#This program demonstrates variable reassignment.
#Assign a value to the dollars variable.
dollars = 2.75
print'I have',dollars,'in my account.'
#Reassign dollars so it references a new value
dollars = 99.95
print 'But now I have',dollars,'in my account!'

#Shows the data type of the variable
print(type(dollars))

#Create variables that reference two strings
first_name = 'Kathryn'
last_name = 'Marino'
print first_name, last_name

#You can also reassign a variable to a different type

x = 99
print x
x = 'Take me to your leader!'
print x

#User input
#Get the user's first name
first_name = raw_input('Enter your first name: ')
#Get the user's last name
last_name = raw_input('Enter your last name: ')
#Print a greeting to the user
print 'Hello',first_name,last_name

#Typecasting
hours = float(input('How many hours did you work last week? '))
print hours

#Get the user's name, age and income.
name = raw_input('What is your name?' )
age = input('What is your age? ')
income = float(input('What is your income? '))

#Display the data
print'Here is the data you entered:'
print'Name:',name
print'Age:',age
print'Income:',income


name = raw_input('Enter you last name: ')
print name

#You need the user of a program to enter the amount of sales for the week. Write a statement that prompts the user to enter this data and assigns the input to a variable.

sales = float(input('Enter the total weekly sales: '))
print sales

#Expressions
# Assign a value to the salary variable.
salary = 2500.0

#Assign a value to the bonus variable.
bonus = 1200.0

#Calculate the total pay by adding the salary and bonus. Assign the result to pay.
pay = salary + bonus

#Display the pay.
print'Your pay is:', pay



