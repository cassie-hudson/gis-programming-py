#Determine the largest of three numbers without using Python functions
#Split function is used to break up strings into smaller strings
x = raw_input("Please enter 3 numbers separated by a comma: ")
x.split(",");
a, b, c =x.split(",")
print a, b, c;

if (a > b AND b > c)



#Import the math library, so you can use the floor function
import math;
#User prompted to choose a conversion
userChoice = raw_input('Enter 1 to convert DD to DMS or 2 to convert DMS to DD: ');
#if 1, calculate these formulas
if(userChoice== "1"):
    DD = float(input('Enter the decimal value you wish to convert: '))
    degrees = math.floor(DD);
    minutes = math.floor(60 * (DD-degrees));
    seconds = 3600 * (DD-degrees) - 60*minutes;
    #print results
    print "Degrees: "+str(degrees) +". Minutes: "+str(minutes)+ ". Seconds: " +str(seconds);
#if 2, do the following calculation and print results
elif (userChoice=="2"):
    Degrees = input('Enter Degrees: ');
    Minutes = input('Enter Minutes: ');
    Seconds = input('Enter Seconds: ');
    dd = Degrees + float(Minutes)/60 + Seconds/3600.0
    print "DD: "+str(dd);
#if not 1 or 2, print and error message
else:
    print 'Please choose 1 or 2.';

