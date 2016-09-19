##Passing the argument

def main():
    fo(100);#Will assign 100 to x
    f1("x", "y", "z"); #Will assign x, y, z to the containers a, b, c
    f1("x","y", 111);
def fo(x):
    print (x);

def f1(a,b,c):
    print (a,b,c);
    print (a);
    print (b);
    print (c);

main();