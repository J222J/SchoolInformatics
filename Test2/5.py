import math as m

sides = eval(input("Enter the number of sides: "))
side = eval(input("Enter the side: "))

area = (sides * side**2)/(4*m.tan(m.pi/sides))
print(f"The area of the polygon is {area:0.2f}")