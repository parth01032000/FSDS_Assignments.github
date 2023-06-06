# Write a Python program to find sum of elements in list?
def calculate_sum(elements):
    total_sum = sum(elements)
    return total_sum

# Example usage
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print("The sum of the elements in the list is:", result)



# Write a Python program to Multiply all numbers in the list?
def multiply_numbers(elements):
    result = 1
    for num in elements:
        result *= num
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print("The multiplication of all numbers in the list is:", result)



# Write a Python program to find smallest number in a list?
def find_smallest_number(elements):
    if len(elements) == 0:
        return None

    smallest = elements[0]
    for num in elements:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_smallest_number(my_list)
print("The smallest number in the list is:", result)



# Write a Python program to find largest number in a list?
def find_largest_number(elements):
    if len(elements) == 0:
        return None

    largest = elements[0]
    for num in elements:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_largest_number(my_list)
print("The largest number in the list is:", result)



# Write a Python program to find second largest number in a list?
def find_second_largest_number(elements):
    if len(elements) < 2:
        return None

    largest = max(elements)
    elements.remove(largest)
    second_largest = max(elements)
    return second_largest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_second_largest_number(my_list)
print("The second largest number in the list is:", result)



# Write a Python program to find N largest elements from a list?
def find_n_largest_elements(elements, n):
    if len(elements) < n:
        return None

    largest_elements = sorted(elements, reverse=True)[:n]
    return largest_elements

# Example usage
my_list = [5, 2, 8, 1, 9, 3, 7]
N = 3
result = find_n_largest_elements(my_list, N)
print("The", N, "largest elements in the list are:", result)



# Write a Python program to print even numbers in a list?
def print_even_numbers(elements):
    even_numbers = []
    for num in elements:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_even_numbers(my_list)
print("Even numbers in the list:", result)



# Write a Python program to print odd numbers in a List?
def print_odd_numbers(elements):
    odd_numbers = []
    for num in elements:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_odd_numbers(my_list)
print("Odd numbers in the list:", result)



# Write a Python program to Remove empty List from List?
def remove_empty_lists(lst):
    result = [sublist for sublist in lst if sublist]
    return result

# Example usage
my_list = [1, 2, [], 3, [], 4, 5, [], [6, 7], []]
result = remove_empty_lists(my_list)
print("List after removing empty lists:", result)




# Write a Python program to Cloning or Copying a list?
def clone_list(lst):
    cloned_list = list(lst)
    return cloned_list

# Example usage
my_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(my_list)
print("Original list:", my_list)
print("Cloned list:", cloned_list)



# Write a Python program to Count occurrences of an element in a list?
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_count = 2
result = count_occurrences(my_list, element_to_count)
print("The element", element_to_count, "occurs", result, "times in the list.")
