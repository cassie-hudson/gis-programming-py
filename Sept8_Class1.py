#There are several ways to print code.
print "Hello";
print 'Hello';
print "'Hello'";
print '"Hello"';
print """'Hello World!'""";

#Output:
#Hello
#Hello
#'Hello'
#"Hello"
#'Hello World!'

#Methods of concatenation

print "Hello"+" "+"World!";
print "Hello","World!";

#Output:
#Hello World!
#Hello World!

#Creating variables

name1 = "Cassie"; #Assigning variables
name2 = 'Hudson';
extension = 8103
print name1, name2; #Prints the values assigned to the variables
print extension;
print type(extension); #Shows the type of the variable

#Output:
#Cassie Hudson
#8103
#<type 'int'>

#User inputs
#name = raw_input("Enter your name: ")--use for string data

num1 = raw_input("Enter number 1: ");
num2 = raw_input('Enter number 2: ');
print num1 + num2; #This concatenates the variables, does not add b/c raw_input dictates that these are string values

#Output:
#Enter number 1: 2
#Enter number 2: 2
#22

num3 = input("Enter number 3: ");
num4 = input("Enter number 4: ");
print num3 + num4;

#By using "input," the numbers are identified as integers and will now be added
#Output
#Enter number 3: 2
#Enter number 4: 2
#4

#You can assign different values to the same variable--reassignment

v1 = 1
v1 = 2
v1 = 3
print v1

#Output:
#3