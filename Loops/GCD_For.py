# Python Program to find the GCD (greatest common divisor) of two numbers.
num1=int(input("Enter the Number 1:\n"))
a=num1
num2=int(input("Enter the Number 2:\n"))
b=num2
x=2
s=1
for j in range(1,num1+num2):
    if num1%x==0 and num2%x==0:
        num1=num1/x
        num2=num2/x
        print(x)
        s=s*x
    else:
        x=x+1
print(f"The GCD (Greatest Common Divisor) of the numbers {a,b} is",s)