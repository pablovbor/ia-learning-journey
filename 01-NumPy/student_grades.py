# In this project , Im going to implement some of the basic functions of numpy mixed to a student's exams data

import numpy as np

grades = np.array([
    [7,8,9],
    [5,6,7],
    [9,9,10],
    [4,5,6],
    [8,7,8]
]) # Dataset of 5 students and their grades in 3 exams

def main():
    print(grades) # Print all grades
    print(grades.shape) # Prints how many students and how many exams are
    print(grades.ndim) # Print the number of dimensions of the grades array

    print(grades[0]) # First student's grade ([7, 8, 9])
    print(grades[0,1]) # First student's second exam grade (8)

    print(grades.mean(axis=1)) # Calculate the average grade for each student
    print(grades.mean(axis=0)) # Calculate the average grade for each exam
main()