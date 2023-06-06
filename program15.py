# Question 1:
# Please write a program using generator to print the numbers which can be divisible by 5 and
# 7 between 0 and n in comma separated form while n is input by console.

def divisible_by_5_and_7(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# Get input from the console
n = int(input("Enter a number (n): "))

# Generate the numbers divisible by 5 and 7
numbers = divisible_by_5_and_7(n)

# Print the numbers in comma-separated form
print(','.join(str(num) for num in numbers))




# Question 2:
# Please write a program using generator to print the even numbers between 0 and n in comma
# separated form while n is input by console.

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Get input from the console
n = int(input("Enter a number (n): "))

# Generate the even numbers
numbers = even_numbers(n)

# Print the numbers in comma-separated form
print(','.join(str(num) for num in numbers))




# Question 3:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n&gt;1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma
# separated form with a given n input by console.

def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers

    # Generate Fibonacci sequence up to n
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]  # Return the first n numbers of the sequence

# Get input from the console
n = int(input("Enter a number (n): "))

# Generate the Fibonacci sequence
sequence = fibonacci_sequence(n)

# Print the sequence in comma-separated form
print(','.join(str(num) for num in sequence))





# Question 4:
# Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
# please write program to print the user name of a given email address. Both user names and
# company names are composed of letters only.

def extract_username(email):
    # Split the email address at the '@' symbol
    parts = email.split('@')

    if len(parts) == 2:
        return parts[0]  # Return the user name
    else:
        return "Invalid email format"  # Return an error message

# Get input from the console
email = input("Enter an email address: ")

# Extract the user name
username = extract_username(email)

# Print the user name
print("User name:", username)





# Question 5:
# Define a class named Shape and its subclass Square. The Square class has an init function
# which takes a length as argument. Both classes have a area function which can print the area
# of the shape where Shape&#39;s area is 0 by default.

class Shape:
    def __init__(self):
        self.area = 0  # Default area is 0
    
    def calculate_area(self):
        pass  # Placeholder method


class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Call the superclass's init method
        self.length = length
    
    def calculate_area(self):
        self.area = self.length ** 2


# Create a Square object
length = float(input("Enter the length of the square: "))
square = Square(length)

# Calculate the area of the square
square.calculate_area()

# Print the area of the square
print("Area of the square:", square.area)
