



try:
    n = input("Enter the final number: ")
    for num in range (1,n):
        print num
except NameError:
    print "Please enter a positive number."