# Write a Python Program to Add Two Matrices?
def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions.")
        return None
    
    # Create a new matrix to store the result
    result = []
    
    # Iterate over the rows of the matrices
    for i in range(len(matrix1)):
        # Create a new row
        row = []
        
        # Iterate over the elements of the row
        for j in range(len(matrix1[0])):
            # Add the corresponding elements from the two matrices
            element_sum = matrix1[i][j] + matrix2[i][j]
            row.append(element_sum)
        
        # Add the row to the result matrix
        result.append(row)
    
    return result

# Example usage
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = add_matrices(matrix1, matrix2)

if result:
    print("The sum of the matrices is:")
    for row in result:
        print(row)



# Write a Python Program to Multiply Two Matrices?
def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None
    
    # Create a new matrix to store the result
    result = []
    
    # Iterate over the rows of the first matrix
    for i in range(len(matrix1)):
        # Create a new row
        row = []
        
        # Iterate over the columns of the second matrix
        for j in range(len(matrix2[0])):
            # Compute the dot product of the corresponding row in the first matrix and column in the second matrix
            dot_product = 0
            for k in range(len(matrix2)):
                dot_product += matrix1[i][k] * matrix2[k][j]
            
            # Add the dot product to the row
            row.append(dot_product)
        
        # Add the row to the result matrix
        result.append(row)
    
    return result

# Example usage
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = multiply_matrices(matrix1, matrix2)

if result:
    print("The product of the matrices is:")
    for row in result:
        print(row)



# Write a Python Program to Transpose a Matrix?
def transpose_matrix(matrix):
    # Get the number of rows and columns of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create a new matrix to store the transposed matrix
    transposed_matrix = []
    
    # Iterate over the columns of the matrix
    for j in range(num_cols):
        # Create a new row
        row = []
        
        # Iterate over the rows of the matrix
        for i in range(num_rows):
            # Add the element at the current column and row to the row
            row.append(matrix[i][j])
        
        # Add the row to the transposed matrix
        transposed_matrix.append(row)
    
    return transposed_matrix

# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = transpose_matrix(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)



# Write a Python Program to Sort Words in Alphabetic Order?
def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

# Example usage
words = ["banana", "apple", "orange", "grapefruit", "cherry"]

sorted_words = sort_words(words)

print("Sorted words:")
for word in sorted_words:
    print(word)



# Write a Python Program to Remove Punctuation From a String?
import string

def remove_punctuation(text):
    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    
    # Remove punctuation from the text using the translation table
    text_without_punctuation = text.translate(translator)
    
    return text_without_punctuation

# Example usage
text = "Hello, world! How are you?"

text_without_punctuation = remove_punctuation(text)

print("Text without punctuation:", text_without_punctuation)
