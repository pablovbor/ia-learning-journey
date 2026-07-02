# In this project, I'm going to apply array reshaping in NumPy

import numpy as np

numbers = np.arange(1, 13) # Create an array of numbers from 1 to 12

def main():
    print(numbers)
    print(numbers.shape) # Print the shape of the original array (12,)
    print(numbers.ndim) # Print the number of dimensions of the original array (1)
    matrix = numbers.reshape(4,3) #Reshape the array to 4 rows and 3 columns
    print(matrix)
    print(matrix.shape) # Print the shape of the reshaped array (4, 3)
    print(matrix.ndim) # Print the number of dimensions of the matrix (2)
    array = matrix.flatten() # Flatten the matrix back to a 1D array
    print(array)

    # Row and column vectors
    column_vector = array.reshape(12, 1)
    row_vector = array.reshape(1, 12)
    print(column_vector)
    print(column_vector.shape) # Column vector is different from array 
    print(row_vector)
    print(row_vector.shape)
main()