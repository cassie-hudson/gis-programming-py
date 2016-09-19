#Global variables

x = 1000;

def main():
    global x;
    fo();
    x = 5; #Will reassign the global variable to 5
    f1();
    fo();
    f1();

def fo():
    global x;
    print (x);
    x = 100; #Will reassign the global variable to 100

def f1():
    global x;
    print (x);

main();

#Local variables

def main():
    fo();
    f1();

def fo():
    x = 10;
    print (x);

def f1():
    x = 100;
    print (x);

#Defining and calling a function
#generate numbers 1 to 10

x = 1
#this will generate numbers 1 to 10, but to be reusable, you should use parameters, not hard values
def generateNos():
    while (x <= 10):
        print x;
#Generic version
def generateNos():
    while (x <= N):
        print x;

#Calling a function by providing its name
generateNos();

#MAIN FUNCTIOn
def main():
    print'main'
    f1();
    f0();

#FUNCTIONS

def f0():
        print
        "function 0";

def f1():
        print
        "function 1";

#Main must be invoked at the end
main();
