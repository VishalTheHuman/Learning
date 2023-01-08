"""Python program to accept a coordinate point in an X-Y coordinate system and determine in
which quadrant the coordinate point lies."""

X_Coordinate=int(input("Enter the X-Coordinate:\n"))
Y_Coordinate=int(input("Enter the Y-Coordinate:\n"))

if X_Coordinate==0 or Y_Coordinate==0:
    print(f"{X_Coordinate,Y_Coordinate} lies on the axis")
elif X_Coordinate==0 and Y_Coordinate==0:
    print(f"{X_Coordinate,Y_Coordinate} lies on the Origin")
elif X_Coordinate>0 and Y_Coordinate>0:
    print(f"{X_Coordinate,Y_Coordinate} lies on the 1st Quadrant")
elif X_Coordinate<0 and Y_Coordinate>0:
    print(f"{X_Coordinate,Y_Coordinate} lies on the 2st Quadrant")
elif X_Coordinate<0 and Y_Coordinate<0:
    print(f"{X_Coordinate,Y_Coordinate} lies on the 3st Quadrant")
else:
    print(f"{X_Coordinate,Y_Coordinate} lies on the 4st Quadrant")