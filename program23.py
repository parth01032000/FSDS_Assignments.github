# Question 1
# Create a function that takes a number as an argument and returns True or False depending
# on whether the number is symmetrical or not. A number is symmetrical when it is the same as
# its reverse.

def is_symmetrical(number):
    return str(number) == str(number)[::-1]

print(is_symmetrical(12321))





# Question 2
# Given a string of numbers separated by a comma and space, return the product of the
# numbers.

def calculate_product(numbers_string):
    numbers = numbers_string.split(", ")
    product = 1
    for num in numbers:
        product *= int(num)
    return product

numbers_string = "2, 3, 4, 5"
product = calculate_product(numbers_string)
print(product)  # Output: 120 (2 * 3 * 4 * 5 = 120)




# Question 3
# Create a function that squares every digit of a number.

def square_digits(number):
    squared_digits = [int(digit) ** 2 for digit in str(number)]
    return int(''.join(map(str, squared_digits)))

number = 1234
result = square_digits(number)
print(result)  # Output: 14916 (1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 14916)




# Question 4
# Create a function that sorts a list and removes all duplicate items from it.

def sort_and_remove_duplicates(lst):
    sorted_lst = sorted(lst)
    unique_lst = list(set(sorted_lst))
    return unique_lst

def sort_and_remove_duplicates(lst):
    sorted_lst = sorted(lst)
    unique_lst = list(set(sorted_lst))
    return unique_lst





# Question 5
# Create a function that returns the mean of all digits.

def digit_mean(number):
    digits = [int(digit) for digit in str(number)]
    mean = sum(digits) / len(digits)
    return mean

number = 12345
result = digit_mean(number)
print(result)  # Output: 3.0 (Mean of digits: (1+2+3+4+5)/5 = 15/5 = 3.0)
