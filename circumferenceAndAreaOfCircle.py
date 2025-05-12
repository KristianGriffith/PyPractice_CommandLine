import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * math.pow(radius,2)

print(f"Circumference = {round(circumference, 2)}cm and area = {round(area, 2)}cm²")

#alt
print(f"Circumference = {circumference:.2f}cm")
