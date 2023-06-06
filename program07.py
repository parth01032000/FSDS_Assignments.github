# Write a Python Program to find sum of array?
def array_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

# Get user input for the array elements
elements = input("Enter the elements of the array (space-separated): ").split()
arr = [int(num) for num in elements]

# Calculate the sum of the array
result = array_sum(arr)

# Print the result
print("The sum of the array is:", result)


# Write a Python Program to find largest element in an array?
def find_largest_element(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]
    for element in arr:
        if element > largest:
            largest = element

    return largest

# Example usage
array = [10, 5, 20, 8, 15]
largest_element = find_largest_element(array)
print("The largest element in the array is:", largest_element)


# Write a Python Program for array rotation?
def rotate_array(arr, rotate_by):
    n = len(arr)
    rotate_by = rotate_by % n  # Ensure rotate_by is within array bounds

    # Rotate the array elements
    rotated_arr = arr[rotate_by:] + arr[:rotate_by]

    return rotated_arr

# Example usage
array = [1, 2, 3, 4, 5]
rotate_by = 2
rotated_array = rotate_array(array, rotate_by)
print("Original array:", array)
print("Rotated array:", rotated_array)



# Write a Python Program to Split the array and add the first part to the end?
def split_and_add(arr, split_index):
    n = len(arr)
    split_index = split_index % n  # Ensure split_index is within array bounds

    # Split the array and add the first part to the end
    splitted_arr = arr[split_index:] + arr[:split_index]

    return splitted_arr

# Example usage
array = [1, 2, 3, 4, 5]
split_index = 2
splitted_array = split_and_add(array, split_index)
print("Original array:", array)
print("Splitted and added array:", splitted_array)



# Write a Python Program to check if given array is Monotonic?
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False

    return increasing or decreasing

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 3, 2, 4, 5]

print("Array 1 is monotonic:", is_monotonic(array1))
print("Array 2 is monotonic:", is_monotonic(array2))
print("Array 3 is monotonic:", is_monotonic(array3))
