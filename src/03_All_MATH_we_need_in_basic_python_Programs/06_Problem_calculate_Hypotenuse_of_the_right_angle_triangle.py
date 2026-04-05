import math

Height = float(input("Enter the Height of the triangle: "))
base = float(input("Enter the length_of_BAse of the triangle: "))

long_side = math.sqrt(pow(Height,2) + pow(base,2))

print(f"The Hypotenuse of the Triangle is {round(long_side,3)}cm")