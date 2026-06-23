# In this project, Im going to operate with two arrays and matrix

import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

matrix = np.array([[1, 2],
                  [3, 4]])
        

def main(a, b, matrix):
    array_sum = a+b # [1+10, 2+20, 3+30]
    array_mul = a*b # [1*10, 2*20, 3*30]
    array_sum_k = a+5 # [1+5, 2+5, 3+5]

    matrix_mul_k = matrix*10 # [1*10, 2*10]
                             # [3*10, 4*10]

    print(f"{array_sum}, {array_mul}, {array_sum_k}, {matrix_mul_k}")

    broadcasted_sum = matrix + np.array([100, 200]) # [1+100, 2+200]
                                                     # [3+100, 4+200]
    print(broadcasted_sum)
main(a, b, matrix)