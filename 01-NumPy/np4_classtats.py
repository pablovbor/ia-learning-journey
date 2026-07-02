# In this project, I'm going to calculate statistical measures from a dataset

import numpy as np

grades = np.array([7, 8, 5, 9, 6, 4, 10, 7, 8, 6])

def main():
    mean_grades = np.mean(grades) # Calculate the mean of the grades
    median_grades = np.median(grades) # Calculate the median of the grades
    standard_deviation = np.std(grades) # Calculate the standard deviation of the grades
    max_grade = np.max(grades) # Calculate the maximum grade
    min_grade = np.min(grades) # Calculate the minimum grade
    per_25 = np.percentile(grades, 25) # Calculate the 25th percentile
    per_75 = np.percentile(grades, 75) # Calculate the 75th percentile
    range_grades = max_grade - min_grade # Calculate the range of the grades
    
    print(f"Mean: {mean_grades}")
    print(f"Median: {median_grades}")
    print(f"Standard Deviation: {standard_deviation}")
    print(f"Max Grade: {max_grade}")
    print(f"Min Grade: {min_grade}")
    print(f"25th Percentile: {per_25}")
    print(f"75th Percentile: {per_75}")
    print(f"Range: {range_grades}")
main()