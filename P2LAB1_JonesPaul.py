#Paul Jones
#6/30/2024
#P2LAB1
#Variables and Expressions
import math

#Get radius user
radius = float(input("Enter the radius: "))

#Calclulate circum, diameter, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")
