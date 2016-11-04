#4.


total = 0
for num in range(10):
    num = input("Enter a number: ")
    total = total + num
    print total
#3.

for num in range(0,1001,10):
    print num


#2.

keep_going = 'y'

while keep_going == 'y':
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    sum = num1 + num2
    print sum
    keep_going = raw_input("Would you like to perform another addition?")



#1.
num = input("Please enter a number: ")

while num < 100:
    num = num*10
    print num

