length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
area = 2 * ((length*width) + (height*length) + (width*height))
volume = length * width * height

print(f"The area of the cuboid is {area} cm^2")
print(f"The volume of the cuboid is {volume}cm^3")