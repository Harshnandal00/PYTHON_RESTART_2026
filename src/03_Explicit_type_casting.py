#typecasting = The process of converting a value of one data type to another
#              (string , integer , float , boolean)
#               Explicit vs implicit


name = "Harsh"
age = 18
gpa = 1.9
student = True


# Explicit typecasting

# Int -> Float
age = float(age)
print(type(age))
print(age)

# Float -> Int
# decimal part is lost during typecasting
gpa = int(gpa)
print(type(gpa))
print(gpa)

# Bool -> Str
# It may seem that output didn't change
# but now the Truth is treated as a string
student = str(student)
print(student)
print(type(student))

# Int -> Bool
# It will always give True as output if value is non-zero
age = bool(age)
print(type(age))
print(age)

# String -> Bool
# If Str is Empty , Bool = False , otherwise True
name = bool(name)
print(type(name))
print(name)