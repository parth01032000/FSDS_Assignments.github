# Question1. Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.

def sum_divisible_by(a, b, c):
    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate over the range from a to b (inclusive)
    for num in range(a, b + 1):
        # Check if the number is evenly divisible by c
        if num % c == 0:
            # Add the number to the sum
            total_sum += num

    # Return the sum
    return total_sum




# Question2. Create a function that returns True if a given inequality expression is correct and
# False otherwise.

def check_inequality(expression):
    try:
        result = eval(expression)
        return result
    except:
        return False

# Example usage
expression1 = "2 + 2 > 4"
expression2 = "5 * 3 <= 17"
expression3 = "10 / 2 != 5"

print(check_inequality(expression1))  # False
print(check_inequality(expression2))  # True
print(check_inequality(expression3))  # False




# Question3. Create a function that replaces all the vowels in a string with a specified character.

def replace_vowels(string, replacement):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for char in string:
        if char in vowels:
            result += replacement
        else:
            result += char

    return result

# Example usage
input_string = "Hello, World!"
replacement_char = "*"

output_string = replace_vowels(input_string, replacement_char)
print(output_string)  # H*ll*, W*rld!





# Question4. Write a function that calculates the factorial of a number recursively.

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = 5
factorial = factorial_recursive(number)
print(factorial)  # 120





# Question 5
# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: &quot;abcbba&quot;
# String2: &quot;abcbda&quot;
# Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
# Create a function that computes the hamming distance between two strings.

def hamming_distance(str1, str2):
    # Check if the strings have equal length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have equal length")

    # Initialize the distance counter
    distance = 0

    # Iterate over each character in the strings
    for char1, char2 in zip(str1, str2):
        # Check if the characters are different
        if char1 != char2:
            distance += 1

    return distance

# Example usage
string1 = "abcbba"
string2 = "abcbda"

distance = hamming_distance(string1, string2)
print(distance)  # Output: 1
