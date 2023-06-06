# Question1
# Write a function that takes a list and a number as arguments. Add the number to the end of
# the list, then remove the first element of the list. The function should then return the updated
# list.

def update_list(lst, number):
    lst.append(number)  # Add the number to the end of the list
    lst.pop(0)  # Remove the first element of the list
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
new_list = update_list(my_list, 6)
print(new_list)  # Output: [2, 3, 4, 5, 6]




# Question2
# Create the function that takes a list of dictionaries and returns the sum of people&#39;s budgets.

def calculate_total_budget(budgets):
    total_budget = 0
    for budget in budgets:
        total_budget += budget['budget']
    return total_budget

# Example usage:
budgets = [
    {'name': 'John', 'budget': 1000},
    {'name': 'Alice', 'budget': 1500},
    {'name': 'Bob', 'budget': 2000}
]

total = calculate_total_budget(budgets)
print(total)  # Output: 4500




# Question3
# Create a function that takes a string and returns a string with its letters in alphabetical order.

def sort_letters(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string

# Example usage:
input_string = "openai"
sorted_string = sort_letters(input_string)
print(sorted_string)  # Output: "aeinop"




# Question4
# Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
# What will be the value of your investment at the end of the 10 year period?
# Create a function that accepts the principal p, the term in years t, the interest rate r, and the
# number of compounding periods per year n. The function returns the value at the end of term
# rounded to the nearest cent.
# For the example above:
# compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
# Note that the interest rate is given as a decimal and n=12 because with monthly compounding
# there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or
# daily.

def compound_interest(p, t, r, n):
    A = p * (1 + r/n)**(n*t)
    return round(A, 2)

# Example usage:
principal = 10000
term = 10
interest_rate = 0.06
compounding_periods = 12

final_amount = compound_interest(principal, term, interest_rate, compounding_periods)
print(final_amount)  # Output: 18193.97




# Question5
# Write a function that takes a list of elements and returns only the integers.

def filter_integers(elements):
    integers = [x for x in elements if isinstance(x, int)]
    return integers

# Example usage:
my_list = [1, 'apple', 3.14, 5, 'banana', 7, 8.8]
integers_only = filter_integers(my_list)
print(integers_only)  # Output: [1, 5, 7]
