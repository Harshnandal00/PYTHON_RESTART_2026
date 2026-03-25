#Default datatype of user input is always string
name = input("Enter your name: ")
# age = input("Enter your age: ")

#  this gives an error as we can't use Mathematical operator in str datatype
#  age = age+1;

# type casting age string into int ..........

# 1st method:
# age = int(age)

# 2nd method :
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")

#  NOw this will not give error as we have type casted it into int from string
age = age+1
print(f"After 1 year...\nyou will be {age} years old")
