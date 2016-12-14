from __future__ import print_function

#5-22

DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print(sale_price)

def get_regular_price():
    price = float(input("Enter the regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()

#Program 5-21 Value-Returning Functions
def main():

    first_age = input("Enter age: ")
    second_age = input("Another age: ")
    total = sum(first_age, second_age)
    print("Together you are", total, "years old.")

def sum(num1, num2):
    result = num1 + num2
    return result
main()


#Program 5-9

def main():
    first_name = raw_input("Enter your first name: ")
    last_name = raw_input("Enter your last name: ")
    print("Your name reversed is: ")
    reverse_name(first_name,last_name)

def reverse_name(first, last):
    print(last, first)

main()


main()
#Program 5-8

def main():
    print("The sum of 12 and 45 is")
    show_sum(12, 45)

def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main()
#Program 5-15

def main():
    intro()
    cups_needed = input("Enter the number of cups: ")
    cups_to_ounces(cups_needed)

def intro():
    print("This program converts measurements\nin cups to fluid ounces. For your\n"
          "reference the formula is:\n1 cup = 8 fluid ounces.")
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")

main()




#Program 5-6

def main():
    value = 5
    show_double(value)

def show_double(number):
    result = number * 2
    print(result)

main()


#Program 5-3
def main():
    startup_message()
    raw_input("Press Enter to see Step 1.")
    step1()
    raw_input("Press Enter to see Step 2.")
    step2()
    raw_input("Press Enter to see Step 3.")
    step3()
    raw_input("Press Enter to see Step 4.")
    step4()

def startup_message():
    print("This program will tell you how to\ndisassemble an ACME laundry dryer.\nThere are four steps in the process.")
    print()

def step1():
    print("Step 1: Unplug the dryer and\nmove it away from the wall.")
    print()

def step2():
    print("Step 2: Remove the six screws\nfrom the back of the dryer.")
    print()

def step3():
    print("Step 3: Remove the back panel\nfrom the dryer.")
    print()

def step4():
    print("Step 4: Pull the top of the\ndryer straight up.")

main()
#Program 5-2
def main():
    print("I have a message for you.")
    message()
    print("Goodbye!")


#Program 5-1
def message ():
    print("I am Arthur,")
    print("King of the Britons.")

message()

main()