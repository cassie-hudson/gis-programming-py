def main():
    a = raw_input("Pleae enter the first string: ")
    b = raw_input("Please enter the second string: ")
    length(a,b)

def length(a,b):
    if len(a) > len(b):
        print a;
    elif len (b) > len(a):
        print b;
    else:
        print a,b;

main();

def main():
    a = raw_input("Pleae enter the first string: ")
    b = raw_input("Please enter the second string: ")
    length(a,b)

def length(a,b):
    print max()

main();

inp = raw_input("Enter a number: ")

n = 1
for digit in inp:
    n = n * int(digit);
print n;





def main():
    a = input("Please enter a value for a: ")
    b = input("Please enter a value for b: ")
    div_by_7(a,b)

def div_by_7(a,b):
    for num in range (a,b):
        if num % 7 == 0:
            print num;

main();