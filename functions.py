import math

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = base * height * .5
    return area

def circle(radius):
    area = math.pi * radius**2
    round_area = round(area, 2)
    return round_area

def rectangle():
    # Get the length and width from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area of the rectangle
    area = length * width

    # Display the result
    print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")

def sqare_perimeter(side):
    return side * 4

def geometry(square_side, circle_radius):
    square_perimeter = square_side * 4
    circle_circumference = circle_radius * 2 * math.pi
    if square_perimeter > circle_circumference:
        return f"The Square has a bigger perimeter than the circumference of the circle"
    else:
        return f"The circle has a bigger circumference than the perimeter of the square"

def dollarizer(word):
    new_string = word.replace("s", "$")
    return new_string

def eurizer(word):
    new_string = word.replace("e", "€")
    return new_string

def replacer(word, char1, char2):
    new_string = word.replace(char1, char2)
    return new_string

def wonky_text(word):
    new_string = word.replace("s", "$").replace("l", "£")
    return new_string

def Cel_to_Fah (Cel):
    Fah = (Cel*9/5) + 32
    return Fah

def age_in_days(years):
    return f"{years * 365} days"

def simple_interest(principal, rate_of_interest, time_in_years):
    total_interest = principal * rate_of_interest * time_in_years
    return total_interest

def plan_finances(principal, rate_of_interest, time_in_years, desired_amount):
    total_interest = principal * rate_of_interest * time_in_years
    if desired_amount < total_interest:
        return "Result not reached :("
    else:
        return "Result reached!"

def calculate_code_time(morning_minutes, evening_hours, evening_minutes):
    total_minutes = morning_minutes + (evening_hours * 60) + evening_minutes
    total_hours = total_minutes / 60
    round_total_hours = round(total_hours, 2)
    return f"\n        *****Congratulations!*****\n\nYou have studied for {total_minutes} minutes OR {round_total_hours} hours\n"

print(calculate_code_time(20, 1, 55))