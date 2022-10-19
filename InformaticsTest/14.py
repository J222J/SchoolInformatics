x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle : "))

side1 = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
side2 = ((x3-x1)**2 + (y3-y1)**2) ** 0.5
side3 = ((x3-x2)**2 + (y3-y2)**2) ** 0.5

p = (side1 + side2 + side3)/2
area = round((p * (p-side1) * (p-side2) * (p-side3)) ** 0.5, 1)

print("The area of the triangle is", area)
