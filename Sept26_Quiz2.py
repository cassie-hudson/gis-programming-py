message = "Hello World";

def f0():
        message = "Welcome to GIS Programming!";
        print message;

def f1():
        global message;
        print message;

def main():
        f0();
        f1();

main();