""" Python Program to find the factorial of N (use recursive function) """

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

terms=int(input("Enter the Number: "))
print(f"The factorial of the number {terms} is {fact(terms)}")
