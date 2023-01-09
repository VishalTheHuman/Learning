"""Python program to find the cube of a number. (use a user defined
function to function to find the cube)."""

def cube(x):
    return x*x*x

num = int(input("Enter a Number:\n"))
print(f"The cube of the Number {num} is {cube(num)}")