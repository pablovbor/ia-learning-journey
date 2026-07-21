# In this project, I'm going to use pandas to sort a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv")
    df = df.sort_values("Age") # Sort by age in ascending order
    print(df)

    df = df.sort_values("Grade", ascending=False) # Sort by grade in descending order
    print(df)

    df = df.sort_values(by=["Age", "Grade"], ascending=[True, False]) # Sort by age (ascending) and grade (descending)
    print(df)
main()