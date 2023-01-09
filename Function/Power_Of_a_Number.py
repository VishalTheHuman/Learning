"""Python program to find the power of a number , x**y
(use a user defined function to function to find the power)."""
def power(x,y):
    if y==1:
        return x
    elif y==0:
        return 1
    else:
        return x*power(x,y-1)

base=int(input("Enter the base Number:\n"))
exp=int(input("Enter the exponent:\n"))
print(f"The base {base} to the power {exp} is {power(base,exp)} ")