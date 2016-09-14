#Prints on a new line, \t adds a tab

print'One\nTwo\nThree'



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



