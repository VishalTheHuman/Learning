# Write a program in Python to display the n terms of square natural number (1, 4, 16, ...) numbers and their sum
sum=0
n=int(input("Enter the Number of terms:\n"))
for n in range(1,n+1):
    sum=sum+n*n
    print(n*n)
print("The sum is",sum)