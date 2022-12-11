import math as m

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input('Enter point 2 (latitude and longitude) in degrees: '))

radius = 6371.01
d = radius * m.acos(m.sin(m.radians(x1))*m.sin(m.radians(x2)) + m.cos(m.radians(x1))*m.cos(m.radians(x2))*m.cos(m.radians(y1-y2)))

print(f"The distance between the two points is {d:0.2f} km")

# 39.55, -116.25
# 41.5, 87.37