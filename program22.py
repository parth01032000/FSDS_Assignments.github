# Question1
# Create a function that takes three parameters where:
#  x is the start of the range (inclusive).
#  y is the end of the range (inclusive).
#  n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n.
# Return an empty list if there are no numbers that are divisible by n.

def find_divisible_numbers(x, y, n):
    divisible_numbers = []
    for num in range(x, y + 1):
        if num % n == 0:
            divisible_numbers.append(num)
    return divisible_numbers

result = find_divisible_numbers(1, 10, 3)
print(result) 



# Question2
# Create a function that takes in two lists and returns True if the second list follows the first list
# by one element, and False otherwise. In other words, determine if the second list is the first
# list shifted to the right by 1.

def is_right_shifted(first_list, second_list):
    if len(first_list) != len(second_list):
        return False

    if first_list[:-1] == second_list[1:]:
        return True

    return False
result = is_right_shifted([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])
print(result)  





# Question3
# A group of friends have decided to start a secret society. The name will be the first letter of
# each of their names, sorted in alphabetical order.
# Create a function that takes in a list of names and returns the name of the secret society.


def secret_society(names):
    initials = [name[0] for name in names]
    secret_name = ''.join(sorted(initials))
    return secret_name

result = secret_society(["Alice", "Bob", "Charlie", "David"])
print(result)  # Output: "ABCD"






# Question4
# An isogram is a word that has no duplicate letters. Create a function that takes a string and
# returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.

def is_isogram(word):
    # Convert the word to lowercase to handle case-insensitive comparison
    word = word.lower()

    # Create a set of unique characters in the word
    unique_chars = set(word)

    # Compare the length of the word with the length of unique characters
    # If they are equal, it means there are no duplicate letters and the word is an isogram
    return len(word) == len(unique_chars)


result = is_isogram("programming")
print(result)





# Question5
# Create a function that takes a string and returns True or False, depending on whether the
# characters are in order or not.

def is_in_order(string):
    # Sort the characters in the string
    sorted_string = sorted(string)

    # Compare the sorted string with the original string
    # If they are equal, it means the characters are in order
    return string == ''.join(sorted_string)

result = is_in_order("abcde")
print(result)