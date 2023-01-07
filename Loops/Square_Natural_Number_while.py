# Write a program in Python to display the n terms of square natural number (1, 4, 16, ...) numbers and their sum Using While Loop
x=1
sum=0
n=int(input("Enter the Number of terms:\n"))
print("\n")
print("The Series is")
while x<=n:
    sum=sum+(x*x)
    print(x*x)
    x=x+1
print("The sum is",sum)
