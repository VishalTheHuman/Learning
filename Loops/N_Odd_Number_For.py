# Write a program in Python to display the n terms of odd natural number and their sum
n=int(input("Number of Terms:\n"))
sum=0
print("The series is")
for x in range(0,n):
    a=2*x + 1
    sum=sum+a
    print(a)

print("The sum is",sum)