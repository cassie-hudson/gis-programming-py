n1 = float (input("Enter number 1: ")); #Float does typecasting (nested statement)
n2 = float (input("Enter number 2: "));
print "Result of sum is: " + str(n1+n2); #Must convert to string to in order to be used with the print statement
print "Result of product is:" + str(n1*n2);
print "Result of subtraction is: ", (n1-n2); #Use , to replace addition sign
res = "Result of division is: "; #assigns the words "Result of division is: " to the res variable
print res+str(n1/n2); #Prints the results of two variables

#Output:
#Enter number 1: 3
#Enter number 2: 3
#Result of sum is: 6.0
#Result of product is:9.0
#Result of subtraction is:  0.0
#Result of division is: 1.0
