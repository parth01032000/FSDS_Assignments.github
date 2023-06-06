# Question1
# Create a function that takes a list of strings and integers, and filters out the list so that it
# returns a list of integers only.

def filter_integers(lst):
    return [x for x in lst if isinstance(x, int)]

my_list = ['apple', 10, 'orange', 25, 30, 'banana', 45]
filtered_list = filter_integers(my_list)
print(filtered_list)


# Question2
# Given a list of numbers, create a function which returns the list but with each element&#39;s
# index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
# number at index 1, etc...

def add_index(lst):
    return [num + index for index, num in enumerate(lst)]

my_list = [10, 20, 30, 40, 50]
modified_list = add_index(my_list)
print(modified_list)




# Question3
# Create a function that takes the height and radius of a cone as arguments and returns the
# volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

import math

def cone_volume(height, radius):
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 2)

cone_height = 5
cone_radius = 3
volume = cone_volume(cone_height, cone_radius)
print(volume)





# Question4
# This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
# The first 5 numbers of the sequence, or dots, are:
# 1, 3, 6, 10, 15

def generate_triangular_sequence(num_terms):
    sequence = []
    for n in range(1, num_terms + 1):
        term = (n * (n + 1)) // 2
        sequence.append(term)
    return sequence

num_terms = 5
triangular_sequence = generate_triangular_sequence(num_terms)
print(triangular_sequence)





# Question5
# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
# returns the missing number.

def find_missing_number(numbers):
    all_numbers = set(range(1, 11))
    given_numbers = set(numbers)
    missing_number = all_numbers - given_numbers
    return list(missing_number)[0]

my_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]
missing_number = find_missing_number(my_list)
print(missing_number)
