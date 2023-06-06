# Write a Python program to check if the given number is a Disarium Number?
def is_disarium_number(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    
    # Calculate the sum of digit^position for each digit
    sum_of_digits = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    
    # Check if the sum is equal to the original number
    if sum_of_digits == number:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_disarium_number(num):
    print(num, "is a Disarium Number.")
else:
    print(num, "is not a Disarium Number.")



# Write a Python program to print all disarium numbers between 1 to 100?
def is_disarium_number(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    
    # Calculate the sum of digit^position for each digit
    sum_of_digits = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    
    # Check if the sum is equal to the original number
    if sum_of_digits == number:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_disarium_number(num):
    print(num, "is a Disarium Number.")
else:
    print(num, "is not a Disarium Number.")




# Write a Python program to check if the given number is Happy Number?
def is_happy_number(number):
    seen_numbers = set()
    
    while True:
        # Calculate the sum of squares of digits
        sum_of_squares = sum(int(digit) ** 2 for digit in str(number))
        
        if sum_of_squares == 1:
            return True
        elif sum_of_squares in seen_numbers:
            return False
        
        # Update the number for the next iteration
        number = sum_of_squares
        seen_numbers.add(number)

# Test the function
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(num, "is a Happy Number.")
else:
    print(num, "is not a Happy Number.")



# Write a Python program to print all happy numbers between 1 and 100?
def is_happy_number(number):
    seen_numbers = set()
    
    while True:
        # Calculate the sum of squares of digits
        sum_of_squares = sum(int(digit) ** 2 for digit in str(number))
        
        if sum_of_squares == 1:
            return True
        elif sum_of_squares in seen_numbers:
            return False
        
        # Update the number for the next iteration
        number = sum_of_squares
        seen_numbers.add(number)

# Find and print all Happy Numbers between 1 and 100
happy_numbers = []
for num in range(1, 101):
    if is_happy_number(num):
        happy_numbers.append(num)

print("Happy numbers between 1 and 100:")
print(happy_numbers)



# Write a Python program to determine whether the given number is a Harshad Number?
def is_harshad_number(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in num_str)
    
    # Check if the number is divisible by the sum of its digits
    if number % sum_of_digits == 0:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad Number.")
else:
    print(num, "is not a Harshad Number.")



# Write a Python program to print all pronic numbers between 1 and 100?
def is_pronic_number(number):
    for i in range(1, int(number**0.5) + 1):
        if i * (i + 1) == number:
            return True
    return False

# Find and print all pronic numbers between 1 and 100
pronic_numbers = []
for num in range(1, 101):
    if is_pronic_number(num):
        pronic_numbers.append(num)

print("Pronic numbers between 1 and 100:")
print(pronic_numbers)
