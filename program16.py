# Question1. Write a function that stutters a word as if someone is struggling to read it. The
# first two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.

def stutter_word(word):
    if len(word) < 2:
        return word
    
    stuttered_word = word[:2] + "... "
    stuttered_word += word[:2] + "... "
    stuttered_word += word + "?"

    return stuttered_word

word = "struggling"
stuttered = stutter_word(word)
print(stuttered)




# Question 2.Create a function that takes an angle in radians and returns the corresponding
# angle in degrees rounded to one decimal place.

import math

def radians_to_degrees(angle_radians):
    angle_degrees = math.degrees(angle_radians)
    rounded_angle = round(angle_degrees, 1)
    return rounded_angle

angle_radians = 1.5708
angle_degrees = radians_to_degrees(angle_radians)
print(angle_degrees)




# Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus
# 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
# number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon
# number, or False otherwise.

def is_curzon_number(num):
    numerator = 2**num + 1
    denominator = 2*num + 1
    
    return numerator % denominator == 0

num = 5
result = is_curzon_number(num)
print(result)




# Question 5. Create a function that returns a base-2 (binary) representation of a base-10
# (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
# 010101001(2) = 1 + 8 + 32 + 128.
# Going from right to left, the value of the most right bit is 1, now from that every bit to the left
# will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

def decimal_to_binary(decimal):
    binary = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    
    return binary

decimal = 157
binary = decimal_to_binary(decimal)
print(binary)
