#Numerical ranges with logical operands
number = input("Please enter a number: ")
if number > 0 and number < 200:
    print "The number is valid."
else:
    print "The number is not valid."


#Loan qualifier using logical operands
min_salary = 30000
min_years = 2

salary = float(input("What is your annual salary?: "))
years = input("How many years have you been at your current job?: ")
if salary >= min_salary or years >= min_years:
    print "You qualify for the loan!"
else:
    print "You do not qualify for this loan."


min_salary = 30000
min_years = 2

salary = float(input("What is your annual salary?: "))
years = input("How many years have you been at your current job?: ")
if salary >= min_salary and years >= min_years:
    print "You qualify for the loan!"
else:
    print "You do not qualify for this loan."




# #if-elif-else Statements
number = input("Enter a number: ")
if number == 1:
    print "One"
elif number == 2:
    print "Two"
elif number == 3:
    print "Three"
else:
    print "Ummm...."

#Nested decision structures
A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = input("Enter your test score: ")
if score >= A_score:
    print "Your grade is A."
else:
    if score >= B_score:
        print "Your grade is B."
    else:
        if score >= C_score:
            print "Your grade is C."
        else:
            if score >= D_score:
                print "Your grade is D."
            else:
                print "You failed!"

min_salary = 30000
min_years = 2

salary = float(input("What is your annual salary?: "))
years = input("How many years have you been at your current job?: ")

if salary >= min_salary:
    if years >= min_years:
        print "You qualify for the loan!"
    else:
        print "You must have been employed for at least", min_years, "to qualify for this loan."
else:
    print "You must earn at least $", format(min_salary, '.2f'), "to qualify for this loan."

#Comparing strings
name1 = raw_input("Enter a name (last name, first name): ")
name2 = raw_input("Enter a name (last name, first name): ")
print "Here are the names, listed alphabetically: "
if name1 < name2:
    print name1
    print name2
else:
    print name2
    print name1

password = raw_input("Enter the password: ")
if password == 'prospero':
    print "Password accepted."
else:
    print "Sorry, that's the wrong password."

#Using the if-else statement
base_hours = 40
ot_multiplier = 1.5
hours = float(input("How many hours did the employee work? "))
pay_rate = float(input("Enter the base pay rate: "))
if hours > base_hours:
    overtime = hours - base_hours
    overtime_pay = overtime * pay_rate * ot_multiplier
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate
print "The gross pay is $", format(gross_pay, ',.2f')

#Using the if statement
high_score = 95
test1 = input("Enter the score for test 1: ")
test2 = input("Enter the score for test 2: ")
test3 = input("Enter the score for test 3: ")
average = (test1 + test2 + test3)/3
print "The average of all the test scores is: ", average
if average >= high_score:
    print "Congratulations!"
    print "That is a great average!"

sales = input("Please enter your total sales: ")
if sales >= 10000:
    commissionRate = 0.2
    print commissionRate

y = input("Please enter a value for y: ")
if y == 20:
    x=0
    print x
