import math

print("select a flat shape to calculate")
print("1. square")
print("2. circle")
print("3. rectangle")
print("4. triangle")
print("5. parallelogram")
print("6. trapezoid")
print("7. rhombus")
print("8. pentagon")
print("9. octagon")
print("10. hexagon")

shape = input("enter choice (1/2/3/4/5/6/7/8/9/10): ")

if shape == "1":
    side = float(input("Enter the side value of the square: "))
    area = side ** 2
    perimeter = side * 4
    print("Area of square: ", area)
    print("Perimeter of square: ", perimeter)
elif shape == "2":
    radius = float(input("Enter the radius value of the circle: "))
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    print("Area of circle: ", area)
    print("Perimeter of circle: ", perimeter)
elif shape == "3":
    length = float(input("Enter the length value of the rectangle: "))
    width = float(input("Enter the width value of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of rectangle: ", area)
    print("Perimeter of rectangle: ", perimeter)
elif shape == "4":
    base = float(input("Enter the base value of the triangle: "))
    height = float(input("Enter the height value of the triangle: "))
    area = 0.5 * base * height
    equilateral = (input("is equilateral? (if yes write yes, if not write no):"))
    if equilateral == "yes":
        side = float(input("Enter the side value of the triangle: "))
        perimeter = 3 * side
        print("Area of triangle: ", area)
        print("Perimeter of triangle: ", perimeter)
    elif equilateral == "no":
        side1 = float(input("Enter the first side value of the triangle: "))
        side2 = float(input("Enter the second side value of the triangle: "))
        side3 = float(input("Enter the third side value of the triangle: "))
        perimeter = side1 + side2 + side3
        print("Area of triangle: ", area)
        print("Perimeter of triangle: ", perimeter)
    else:
        print("wrong equilateral input")    
elif shape == "5":
    base = float(input("Enter the base value of the parallelogram: "))
    height = float(input("Enter the height value of the parallelogram: "))
    area = base * height
    perimeter = 2 * (base + height)
    print("Area of parallelogram: ", area)
    print("Perimeter of parallelogram: ", perimeter)
elif shape == "6":
    height = float(input("Enter the height value of the trapezoid: "))
    base1 = float(input("Enter the first base value of the trapezoid: "))
    base2 = float(input("Enter the second base value of the trapezoid: "))
    side1 = float(input("Enter the first side value of the trapezoid: "))
    side2 = float(input("Enter the second side value of the trapezoid: "))
    area = 0.5 * (side1 + side2) * height
    perimeter = side1 + side2 + base1 + base2
    print("Area of trapezoid: ", area)
    print("Perimeter of trapezoid: ", perimeter)
elif shape == "7":
    diagonal1 = float(input("Enter the first diagonal value of the rhombus: "))
    diagonal2 = float(input("Enter the second diagonal value of the rhombus: "))
    side = float(input("Enter the side value of the rhombus: "))
    area = 0.5 * diagonal1 * diagonal2
    perimeter = 4 * side
    print("Area of rhombus: ", area)
    print("Perimeter of rhombus: ", perimeter)
elif shape in ['8', '9', '10']:
    side = float(input("Enter the side value of the shape: "))
    if shape == "8":
        area = 0.25 * ((5 * (5 + (2 * (5 ** 0.5)))) ** 0.5) * side ** 2
        perimeter = 5 * side
    elif shape == ("9"):
        area = ((3 * (3 ** 0.5)) / 2) * (side ** 2)
        perimeter = 6 * side
    else: #shape ("10")
        area = (2 * (1+ (2 ** 0.5))) * (side ** 2)
        perimeter = 8 * side
    print("Area of shape: ", area)
    print("Perimeter of shape: ", perimeter)
else:
    print("wrong shape input")    








