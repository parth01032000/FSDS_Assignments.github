# Write a Python program to find words which are greater than given length k?
def find_words_greater_than_length(sentence, k):
    words = sentence.split()
    result = []
    
    for word in words:
        if len(word) > k:
            result.append(word)
    
    return result

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog"
length_threshold = 4
words_greater_than_length = find_words_greater_than_length(input_sentence, length_threshold)
print(f"Words greater than length {length_threshold}: {words_greater_than_length}")



# Write a Python program for removing i-th character from a string?
def remove_character(string, i):
    if i < 0 or i >= len(string):
        return string  # i is out of range, return the original string
    else:
        return string[:i] + string[i+1:]

# Example usage:
input_string = "Hello, World!"
index_to_remove = 7
result = remove_character(input_string, index_to_remove)
print(result)



# Write a Python program to split and join a string?
def split_and_join(string, delimiter):
    # Split the string into a list of substrings using the specified delimiter
    words = string.split(delimiter)

    # Join the list of substrings into a single string using a space as the separator
    joined_string = " ".join(words)

    return joined_string

# Example usage:
input_string = "Hello,World!This,is,a,string."
delimiter = ","
result = split_and_join(input_string, delimiter)
print(result)



# Write a Python to check if a given string is binary string or not?
def is_binary_string(string):
    for char in string:
        if char != '0' and char != '1':
            return False
    return True

# Example usage:
input_string = "101010"
result = is_binary_string(input_string)
if result:
    print("The string is a binary string.")
else:
    print("The string is not a binary string.")



# Write a Python program to find uncommon words from two Strings?
def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    
    uncommon_words = words1.symmetric_difference(words2)
    
    return uncommon_words

# Example usage:
string1 = "Hello world! This is string 1."
string2 = "This is string 2. Hello world!"
result = find_uncommon_words(string1, string2)
print(result)



# Write a Python to find all duplicate characters in string?
def find_duplicate_characters(string):
    duplicate_characters = []
    character_count = {}

    # Count the occurrence of each character in the string
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    # Find the characters with count greater than 1 (duplicates)
    for char, count in character_count.items():
        if count > 1:
            duplicate_characters.append(char)

    return duplicate_characters

# Example usage:
input_string = "Hello, World!"
result = find_duplicate_characters(input_string)
print(result)



# Write a Python Program to check if a string contains any special character?
import re

def has_special_characters(input_string):
    special_characters_regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_characters_regex.search(input_string) is not None

# Example usage
input_string = "Hello World!"
contains_special_characters = has_special_characters(input_string)
print(f"String '{input_string}' contains special characters: {contains_special_characters}")
