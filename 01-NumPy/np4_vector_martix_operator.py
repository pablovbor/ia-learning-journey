# In this project, I'm going to operate on vectors and matrices using NumPy. 

import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
grades = np.array([[5, 5, 7.5], [4.25, 6.75, 8.5], [3.5, 4.25, 6.75]])
weights = np.array([0.2, 0.3, 0.5])
def main():
    print(v1+v2) # Adding two vectors
    print(v1-v2) # Subtracting two vectors
    print(v1*v2) # Element-wise multiplication of two vectors
    print(v1/v2) # Element-wise division of two vectors
    print(np.dot(v1, v2)) # Dot product of two vectors

    print(m1 @ m2) # Matrix multiplication
    print(np.matmul(m1, m2)) # Another way to perform matrix multiplication
    print(m1.T) # Transpose of a matrix
    print(m2.T)
    print(np.dot(grades, weights)) # Weighted average of grades using dot product
main()