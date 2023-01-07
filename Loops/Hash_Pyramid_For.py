# Python program to Print a hash(#) triangle / hash pyramid (for Loop)
n=int(input("Enter the Number of rows for the Pyramid:\n"))
k=1
for x in range(1,n+1):
    for h  in range(1,x+1):
        print("#",end="")
        k=k+1
    print("\n")