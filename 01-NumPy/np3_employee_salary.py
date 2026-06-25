# In this project, Im going to aplicate filtros to an employees dataset that is like this: [age, annual salary]
import numpy as np

employees = np.array([
    [25, 25000],
    [40, 45000],
    [30, 32000],
    [50, 60000],
    [22, 22000],
    [43, 45000],
    [28, 32000],
    [24, 22000],
    [26, 60000],
    [48, 28000]
])

def main():
    salary_filter = employees[:, 1] > 30000 # # Filter employees with a salary above 30000
    age_filter = employees[:, 0] > 30 # # Filter employees older than 30
    print(employees[salary_filter]) # Print employees with a salary above 30000 
    print(employees[age_filter]) # Print employees older than 30
    print(employees[salary_filter & age_filter]) # Print employees with salary about 30000 and older than 30
main()