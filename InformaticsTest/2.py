from math import pi

radius, length = eval(input("Enter the radius and the length of a cylinder : "))

area = pi * radius**2
volume = area * length

print("The area is", area)
print("The volume is", volume)