# Question1
# Create a function that takes an integer and returns a list from 1 to the given number, where:
# 1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
# number).
# 2. If the number cannot be divided evenly by 4, simply return the number.

def amplify_numbers(num):
    result = []
    for i in range(1, num + 1):
        if i % 4 == 0:
            result.append(i * 10)
        else:
            result.append(i)
    return result

print(amplify_numbers(10))  # Output: [1, 2, 3, 40, 5, 6, 7, 80, 9, 10]
print(amplify_numbers(20))  # Output: [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 12, 13, 160, 15, 16, 17, 200, 19, 20]





# Question2
# Create a function that takes a list of numbers and return the number that&#39;s unique.

def find_unique_number(numbers):
    count_dict = {}
    
    # Count the occurrences of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the number with count 1
    for num, count in count_dict.items():
        if count == 1:
            return num
    
    # If no unique number found, return None or any other value as desired
    return None

numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_number = find_unique_number(numbers)
print(unique_number)  # Output: 1

numbers = [1, 2, 2, 3, 3, 4, 4]
unique_number = find_unique_number(numbers)
print(unique_number)  # Output: None






# Question3
# Your task is to create a Circle constructor that creates a circle with a radius provided by an
# argument. The circles constructed must have two getters getArea() (PIr^2) and
# getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

# For help with this class, I have provided you with a Rectangle constructor which you can use
# as a base example.


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
area = circle.getArea()
perimeter = circle.getPerimeter()

print("Area:", area)  # Output: Area: 78.53981633974483
print("Perimeter:", perimeter)  # Output: Perimeter: 31.41592653589793






# Question4
# Create a function that takes a list of strings and return a list, sorted from shortest to longest.

def sort_strings_by_length(strings):
    return sorted(strings, key=len)

strings = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)





# Question5
# Create a function that validates whether three given integers form a Pythagorean triplet. The
# sum of the squares of the two smallest integers must equal the square of the largest number to
# be validated.

def is_pythagorean_triplet(a, b, c):
    # Find the squares of the three numbers
    square_a = a ** 2
    square_b = b ** 2
    square_c = c ** 2
    
    # Check the Pythagorean theorem
    if square_a + square_b == square_c or square_b + square_c == square_a or square_c + square_a == square_b:
        return True
    else:
        return False

print(is_pythagorean_triplet(3, 4, 5))  # Output: True
print(is_pythagorean_triplet(5, 12, 13))  # Output: True
print(is_pythagorean_triplet(4, 7, 9))  # Output: False






