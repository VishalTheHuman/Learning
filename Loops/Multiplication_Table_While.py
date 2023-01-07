# Write a program in Python to display the multiplication table of a given integer.
x=1
n=int(input("Enter the Number:\n")) # Multiplier
k=int(input("Enter the Maximum Limit:\n")) #Maximum Multiplicand

while x<=k:
    print(x,"x",n,"=",x*n)
    x=x+1