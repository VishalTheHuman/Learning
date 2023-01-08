""" Python program to input the angles of a triangle and check whether the triangle is valid or
not. """
A1=int(input("Enter Angle 1:\n"))
A2=int(input("Enter Angle 2:\n"))
A3=int(input("Enter Angle 3:\n"))

sum=A1+A2+A3
if sum ==180 :
    print("Angles are valid")
else:
    print("Angles are invalid")