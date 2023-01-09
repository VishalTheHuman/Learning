# The volume of a sphere with radius r is (4/3)*pi*r³. What is the voulme of sphere r?
def spherevolume(r):
    pi=22/7
    return (4/3)*pi*(r**3)

r=int(input("Enter  the Radius of the Sphere: "))
print(f"The Voulme of the sphere with the radius {r} is {spherevolume(r)} cubic units.")