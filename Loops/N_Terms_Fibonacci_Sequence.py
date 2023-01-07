# Printing N Terms of the Fibonacci series using Python
sum=0
t0=1
t1=1
n=int(input("Enter the Number of Terms:\n"))
print("\n")
if n==0:
    print("Invalid")
elif n==1:
    print("1")
elif n==2:
    print("1 1")
else:
    print("1")
    for a in range(1,n):
        sum=sum+t0
        t0=t1
        t1=sum
        print(sum)
