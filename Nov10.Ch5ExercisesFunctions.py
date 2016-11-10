from __future__ import print_function



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