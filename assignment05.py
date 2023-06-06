# Write a Python Program to Find LCM?

def calculate_lcm(num1, num2):
    # Find the greater number
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm


# Write a Python Program to Find HCF?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", result)


def calculate_hcf(num1, num2):
    # Find the smaller number
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2

    hcf = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf


# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", result)

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)


# Write a Python Program To Find ASCII value of a character?
character = input("Enter a character: ")
ascii_value = ord(character)

print("The ASCII value of", character, "is", ascii_value)


# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "*"
elif choice == '4':
    result = divide(num1, num2)
    operation = "/"

print(num1, operation, num2, "=", result)
