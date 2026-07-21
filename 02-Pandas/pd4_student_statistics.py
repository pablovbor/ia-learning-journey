# In this project, I'm going to use pandas to calculate descriptive statistics from a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv")

    highest_grade = df["Grade"].max()  # Get the highest grade
    print(highest_grade)

    lowest_grade = df["Grade"].min()  # Get the lowest grade
    print(lowest_grade)

    total_age = df["Age"].sum()  # Calculate the sum of all students' ages
    print(total_age)

    average_grade = df["Grade"].mean()  # Calculate the average grade
    print(average_grade)

    median_grade = df["Grade"].median()  # Calculate the median grade
    print(median_grade)

    most_common_career = df["Career"].mode()  # Get the most common career
    print(most_common_career)

    highest_grade_index = df["Grade"].idxmax()  # Get the index of the highest grade
    print(highest_grade_index)

    lowest_grade_index = df["Grade"].idxmin()  # Get the index of the lowest grade
    print(lowest_grade_index)

main()