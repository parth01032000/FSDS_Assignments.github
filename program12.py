# Write a Python program to Extract Unique values dictionary values?
def extract_unique_values(dictionary):
    unique_values = set()

    for values in dictionary.values():
        if isinstance(values, list):
            unique_values.update(values)
        else:
            unique_values.add(values)

    return unique_values


# Example usage:
my_dict = {
    "key1": "value1",
    "key2": ["value2", "value3"],
    "key3": "value4",
    "key4": ["value2", "value5"]
}

unique_values = extract_unique_values(my_dict)
print(unique_values)



# Write a Python program to find the sum of all items in a dictionary?
def sum_of_dictionary_items(dictionary):
    total_sum = 0

    for value in dictionary.values():
        total_sum += value

    return total_sum


# Example usage:
my_dict = {
    "item1": 10,
    "item2": 5,
    "item3": 8,
    "item4": 3
}

result = sum_of_dictionary_items(my_dict)
print("Sum of dictionary items:", result)



# Write a Python program to Merging two Dictionaries?
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged)



# Write a Python program to convert key-values list to flat dictionary?
def convert_to_flat_dictionary(key_value_list):
    flat_dict = {}

    for pair in key_value_list:
        key, value = pair
        flat_dict[key] = value

    return flat_dict


# Example usage:
key_value_list = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]

flat_dictionary = convert_to_flat_dictionary(key_value_list)
print("Flat Dictionary:", flat_dictionary)



# Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    ordered_dict.update({key: value})
    ordered_dict.move_to_end(key, last=False)

# Example usage:
my_ordered_dict = OrderedDict([('key1', 'value1'), ('key2', 'value2')])

print("Original OrderedDict:", my_ordered_dict)

insert_at_beginning(my_ordered_dict, 'key3', 'value3')
print("Modified OrderedDict:", my_ordered_dict)



# Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict

def check_order_of_characters(string, pattern):
    pattern_dict = OrderedDict.fromkeys(pattern)

    j = 0
    for char in string:
        if j >= len(pattern):
            break
        if char == pattern[j]:
            j += 1

    return j == len(pattern)

# Example usage:
input_string = "Hello, World!"
input_pattern = "llo"

result = check_order_of_characters(input_string, input_pattern)
print("Pattern order in string:", result)



# Write a Python program to sort Python Dictionaries by Key or Value?
def sort_dictionary_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    return sorted_dict


def sort_dictionary_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict


# Example usage:
my_dict = {"b": 2, "c": 3, "a": 1}

sorted_by_key = sort_dictionary_by_key(my_dict)
print("Sorted by Key:", sorted_by_key)

sorted_by_value = sort_dictionary_by_value(my_dict)
print("Sorted by Value:", sorted_by_value)
