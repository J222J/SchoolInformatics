import math as m

side = eval(input("Enter the side: "))

area = (5 * side**2)/(4*m.tan(m.pi/5))
print(f"The area of the pentagon is {area:0.2f}")