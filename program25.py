# Question1
# Create a function that takes three integer arguments (a, b, c) and returns the amount of
# integers which are of equal value.

def count_equal_integers(a, b, c):
    count = 0
    if a == b == c:
        count = 3
    elif a == b or b == c or a == c:
        count = 2
    return count

result = count_equal_integers(5, 5, 5)
print(result)  # Output: 3





# Question2
# Write a function that converts a dictionary into a list of keys-values tuples.

def convert_dict_to_tuples(dictionary):
    return list(dictionary.items())

my_dict = {'a': 1, 'b': 2, 'c': 3}
result = convert_dict_to_tuples(my_dict)
print(result)





# Question3
# Write a function that creates a dictionary with each (key, value) pair being the (lower case,
# upper case) versions of a letter, respectively.

def create_letter_dictionary():
    letter_dict = {}
    for letter in range(ord('a'), ord('z')+1):
        lowercase = chr(letter)
        uppercase = lowercase.upper()
        letter_dict[lowercase] = uppercase
    return letter_dict

result = create_letter_dictionary()
print(result)






# Question4
# Write a function, that replaces all vowels in a string with a specified vowel.

def replace_vowels(string, replacement):
    vowels = 'aeiouAEIOU'
    replaced_string = ''
    for char in string:
        if char in vowels:
            replaced_string += replacement
        else:
            replaced_string += char
    return replaced_string

my_string = 'Hello, world!'
result = replace_vowels(my_string, 'x')
print(result)





# Question5
# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
# and returns its lower case version if its ASCII code is odd.

def capitalize_by_ascii(string):
    capitalized_string = ''
    for char in string:
        if ord(char) % 2 == 0:
            capitalized_string += char.upper()
        else:
            capitalized_string += char.lower()
    return capitalized_string

my_string = 'Hello, world!'
result = capitalize_by_ascii(my_string)
print(result)
