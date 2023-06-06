# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.

import math

C = 50
H = 30

def calculate_Q(D):
    Q = math.sqrt((2 * C * D) / H)
    return Q

input_sequence = input("Enter comma-separated values for D: ")
D_values = input_sequence.split(',')

for D in D_values:
    result = calculate_Q(float(D))
    print("Q =", result)



# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.

def generate_array(X, Y):
    array = [[i * j for j in range(Y)] for i in range(X)]
    return array

X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))

result = generate_array(X, Y)

print("Generated 2-dimensional array:")
for row in result:
    print(row)



# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetical

input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split(',')

sorted_words = sorted(words)

output_sequence = ','.join(sorted_words)

print("Sorted words:", output_sequence)



# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.

input_sequence = input("Enter a sequence of whitespace-separated words: ")
words = input_sequence.split()

unique_words = list(set(words))
sorted_words = sorted(unique_words)

output_sequence = ' '.join(sorted_words)

print("Sorted words (after removing duplicates):", output_sequence)




# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.

sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)



# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them
# according to the above criteria. Passwords that match the criteria are to be printed, each
# separated by a comma.

import re

def check_password_validity(password):
    if len(password) < 6 or len(password) > 12:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[$#@]", password):
        return False

    return True

passwords = input("Enter comma-separated passwords: ")
password_list = passwords.split(',')

valid_passwords = []

for password in password_list:
    if check_password_validity(password):
        valid_passwords.append(password)

output_sequence = ', '.join(valid_passwords)

print("Valid passwords:", output_sequence)
