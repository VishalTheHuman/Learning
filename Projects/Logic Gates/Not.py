# Not Gate

a=int(input("Enter an Input:"))
if a>1 or a<0:
    while a==0 or a==1:
        a=int(input("Enter an Input:"))

def Not(x):
    if x==1:
        return 0
    elif x==0:
        return 1
    else:
        print("Invalid Inputs")
        return Not(x)

print(f"The Not Logic of {a} is {Not(a)}")

