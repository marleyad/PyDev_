import math

def circle():
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle: "))

    # Calculate the area of the circle
    area = math.pi * radius**2

    # Display the result
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

def rectangle():
    # Get the length and width from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area of the rectangle
    area = length * width

    # Display the result
    print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")


shape = input("\n\nWhat shape do you want me to figure the area of?\n\nChoose a shape (Circle, Rectangle): ").lower()

if shape == "circle":
    circle()
else:
    rectangle()