# Question 1:
# Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven_generator(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num



# Question 2:
# Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically.

def word_frequency(input_text):
    # Split the input text into words
    words = input_text.split()

    # Create a dictionary to store word frequencies
    frequency_dict = {}

    # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    # Sort the frequency dictionary by keys in alphabetical order
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[0])

    # Print the sorted frequency counts
    for word, frequency in sorted_freq:
        print(f"{word}: {frequency}")

# Take user input
input_text = input("Enter the input text: ")

# Call the function to compute word frequencies and print the sorted counts
word_frequency(input_text)




# Question 3:

# Define a class Person and its two child classes: Male and Female. All classes have a
# method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
# class.

class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

person = Person()
person.getGender() 



# Question 4:
# Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
# verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = []

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            sentences.append(sentence)

# Print all generated sentences
for sentence in sentences:
    print(sentence)





# Question 5:
# Please write a program to compress and decompress the string &quot;hello world!hello
# world!hello world!hello world!&quot;.

import zlib

def compress_string(string):
    # Convert the string to bytes
    byte_string = string.encode('utf-8')

    # Compress the byte string
    compressed_data = zlib.compress(byte_string)

    # Convert the compressed data to a string
    compressed_string = compressed_data.decode('utf-8')

    return compressed_string

def decompress_string(compressed_string):
    # Convert the compressed string to bytes
    compressed_data = compressed_string.encode('utf-8')

    # Decompress the byte string
    decompressed_data = zlib.decompress(compressed_data)

    # Convert the decompressed data to a string
    decompressed_string = decompressed_data.decode('utf-8')

    return decompressed_string

# Define the input string
input_string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_string = compress_string(input_string)
print("Compressed string:", compressed_string)

# Decompress the string
decompressed_string = decompress_string(compressed_string)
print("Decompressed string:", decompressed_string)




# Question 6:
# Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.

def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    # Item not found in the list
    return -1

# Sorted list
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Item to search for
target = 10

# Perform binary search
result = binary_search(my_list, target)

if result != -1:
    print(f"Item {target} found at index {result}.")
else:
    print(f"Item {target} not found in the list.")
