"""Write a program in Python to make such a pattern like a pyramid with numbers increased
by 1. Take input as the number of rows of the pyramid"""

rows=int(input("Enter the Number of the Rows:\n"))
z=1
for x in range(1,rows+1):
    for y in range(1,x+1):
        print(f" ",z,end="")
        z=z+1
    print("\n")