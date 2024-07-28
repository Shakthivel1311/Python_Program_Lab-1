import math

def calculate_area(a, b, c):
 
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))

a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))


area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)

total_area = area1 + area2

contribution1 = (area1 / total_area) * 100
contribution2 = (area2 / total_area) * 100

print(f"Area of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"Contribution of the first triangle: {contribution1:.2f}%")
print(f"Contribution of the second triangle: {contribution2:.2f}%")
