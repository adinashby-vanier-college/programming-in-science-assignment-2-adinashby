# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)   # Sort in descending order
    max_value = unique_numbers[0]       # First element is the max
    second_max = unique_numbers[1] if len(unique_numbers) > 1 else None  # Second max if available
    return max_value, second_max

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num  # Add each element to the running total
        result.append(total)  # Store the cumulative sum
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]  # Initialize the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]  # Swap rows and columns
    return transposed

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return [lst[i] for i in range(0, len(lst), step)]  # Iterate with step size

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0
    for x, y in zip(list1, list2):
        total += x * y  # Multiply element-wise and sum
    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])
    
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]  # Initialize result matrix
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Multiply and accumulate
    
    return result
