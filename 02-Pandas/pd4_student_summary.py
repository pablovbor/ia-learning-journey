# In this project, I'm going to use pandas to get information about a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv")
    careers = df["Career"].unique() # Get all unique career names
    print(careers)

    careers_number = df["Career"].nunique() # Count all unique careers
    print(careers_number)

    careers_freq = df["Career"].value_counts() # Count how many times any career appears
    print(careers_freq)

    careers_percentages = df["Career"].value_counts(normalize=True) # # Calculate the percentage of each career
    print(careers_percentages)
main()