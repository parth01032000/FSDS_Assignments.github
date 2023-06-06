# Question 1
# Create a function that takes a list of non-negative integers and strings and return a new list
# without the strings.

def filter_non_negative(lst):
    return [x for x in lst if isinstance(x, int)]

# Example usage:
my_list = [1, 2, "three", 4, "five", 6]
filtered_list = filter_non_negative(my_list)
print(filtered_list)




# Question 2
# The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
# opposite case.

def reverser(string):
    reversed_string = string[::-1]  # Reverse the string using slicing
    reversed_string = reversed_string.swapcase()  # Swap the case of characters
    return reversed_string

# Example usage:
input_string = "Hello, World!"
reversed_string = reverser(input_string)
print(reversed_string)




# Question 3
# You can assign variables from lists like this:

writeyourcodehere = [1, 2, 3, 4, 5, 6]
first, *middle, last = writeyourcodehere

print(first)    # Output: 1
print(middle)   # Output: [2, 3, 4, 5]
print(last)     # Output: 6





# Question 4
# Write a function that calculates the factorial of a number recursively.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
result = factorial(number)
print(result)






# Question 5
# Write a function that moves all elements of one type to the end of the list.

def move_elements_to_end(lst, element_type):
    count = lst.count(element_type)  # Count the occurrences of the given element type
    lst = [elem for elem in lst if elem != element_type]  # Remove the elements of the given type
    lst.extend([element_type] * count)  # Append the elements of the given type to the end
    return lst

# Example usage:
my_list = [1, 2, 3, 'a', 'b', 4, 'c', 5]
element_type = 'b'
new_list = move_elements_to_end(my_list, element_type)
print(new_list)
