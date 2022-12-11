import math as m

ax, ay, gx, gy, ox, oy, fx, fy = 33.748997, -84.387985, 32.165623, -82.900078, 28.538336, -81.379234, 27.664827, -81.515755

radius = 6371.01
a = radius * m.acos(m.sin(m.radians(ax))*m.sin(m.radians(gx)) + m.cos(m.radians(ax))*m.cos(m.radians(gx))*m.cos(m.radians(ay-gy)))
b = radius * m.acos(m.sin(m.radians(ax))*m.sin(m.radians(fx)) + m.cos(m.radians(ax))*m.cos(m.radians(fx))*m.cos(m.radians(ay-fy)))
c = radius * m.acos(m.sin(m.radians(gx))*m.sin(m.radians(ox)) + m.cos(m.radians(gx))*m.cos(m.radians(ox))*m.cos(m.radians(gy-oy)))
d = radius * m.acos(m.sin(m.radians(ox))*m.sin(m.radians(fx)) + m.cos(m.radians(ox))*m.cos(m.radians(fx))*m.cos(m.radians(oy-fy)))
e = radius * m.acos(m.sin(m.radians(fx))*m.sin(m.radians(gx)) + m.cos(m.radians(fx))*m.cos(m.radians(gx))*m.cos(m.radians(fy-gy)))

p1 = a+e+d
p2 = b+c+e

area1 = m.sqrt(p1*(p1-a)*(p1-e)*(p1-d))
area2 = m.sqrt(p2*(p2-b)*(p2-c)*(p2-e))
areat = area1+area2

print(f"The area between Atlanta, Georgia, Orlando and Florida is: {areat:0.2f} km^2")