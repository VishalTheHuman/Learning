"""Write a program in Python to make such a pattern like a pyramid with numbers increased
by 1. Take input as the number of rows of the pyramid"""

def spaces(a):
    for a in range (1,a+1):
        print(" ",end="")

rows=int(input("Enter the Number of the Rows:\n"))
z=1
print("\n Pyramid\n")
for x in range(1,rows+1):
    spaces(rows-x)
    for y in range(1,x+1):
        
        print(f" ",z,end="")
        z=z+1
    print("\n")

