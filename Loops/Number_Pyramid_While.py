# Python program to Print a Number triangle / hash pyramid (while Loop)
n=int(input("Enter the Number of rows for the Pyramid:\n"))
x=1
h=1
print("\nPyramid\n")
while x<= n:
    h=1
    while h <= x:
        print(h,end="")
        h=h+1
    print("\n")
    x=x+1 

