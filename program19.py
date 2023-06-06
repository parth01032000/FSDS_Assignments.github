# Question1
# Create a function that takes a string and returns a string in which each character is repeated
# once.

def repeat_characters(input_string):
    repeated_string = ""
    for char in input_string:
        repeated_string += char * 2
    return repeated_string

input_str = "Hello, World!"
result = repeat_characters(input_str)
print(result)





# Question2
# Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
# if another variable type is given.

def reverse_boolean(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"

result1 = reverse_boolean(True)
print(result1)  




# Question3
# Create a function that returns the thickness (in meters) of a piece of paper after folding it n
# number of times. The paper starts off with a thickness of 0.5mm.

def calculate_paper_thickness(fold_count):
    initial_thickness_mm = 0.5
    final_thickness_m = initial_thickness_mm / 1000  # Convert initial thickness from mm to meters

    for _ in range(fold_count):
        final_thickness_m *= 2

    return final_thickness_m

thickness1 = calculate_paper_thickness(0)
print(thickness1) 





# Question4

# Create a function that takes a single string as argument and returns an ordered list containing
# the indices of all capital letters in the string.

def get_capital_indices(input_string):
    capital_indices = []
    for index, char in enumerate(input_string):
        if char.isupper():
            capital_indices.append(index)
    return capital_indices


input_str = "Hello World! How Are You?"
result = get_capital_indices(input_str)
print(result)







# Question5
# Using list comprehensions, create a function that finds all even numbers from 1 to the given
# number.

def find_even_numbers(n):
    even_numbers = [x for x in range(1, n + 1) if x % 2 == 0]
    return even_numbers

n = 10
result = find_even_numbers(n)
print(result)
