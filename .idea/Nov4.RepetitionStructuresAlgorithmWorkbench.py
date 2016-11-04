from __future__ import print_function
#9.

num = input("Enter a number between 1 and 100: ")

while num < 1 or num > 100:
    print('Error! You have entered an invalid number.')
    num = input("Enter a number between 1 and 100.")
#8.
num = input("Enter a positive, non-zero number: ")

while num <= 0:
    print("Error: Please enter a positive, non-zero number.")
    num = input("Enter a positive, non-zero number: ")


#7.



for rows in range (10):
    for cols in range (15):
        print ('#', end=' ')
    print( )

