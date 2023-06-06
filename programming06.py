# Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def display_fibonacci_sequence(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(count):
            print(fibonacci(i))

# Get user input for the count of Fibonacci numbers to display
num_count = int(input("Enter the number of Fibonacci numbers to display: "))

# Call the function to display the Fibonacci sequence
display_fibonacci_sequence(num_count)


# Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")


# Write a Python Program to calculate your Body Mass Index?
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Print the result
print("Your Body Mass Index (BMI) is:", bmi)


# Write a Python Program to calculate the natural logarithm of any number?
import math

# Get user input for the number
num = float(input("Enter a number: "))

# Calculate the natural logarithm
logarithm = math.log(num)

# Print the result
print("The natural logarithm of", num, "is", logarithm)


# Write a Python Program for cube sum of first n natural numbers?
def cube_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum

# Get user input for the value of n
n = int(input("Enter the value of n: "))

# Calculate the cube sum
result = cube_sum(n)

# Print the result
print("The cube sum of the first", n, "natural numbers is", result)
