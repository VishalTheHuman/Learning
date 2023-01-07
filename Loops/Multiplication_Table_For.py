# Write a program in Python to display the multiplication table of a given integer.

n=int(input("Enter the Number:\n"))
k=int(input("Enter the Maximum Limit:\n")) #Maximum Multiplicand

for x in range(1,k+1):
    print(x,"x",n,"=",x*n)