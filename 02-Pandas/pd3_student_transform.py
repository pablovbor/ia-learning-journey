# In this project, I'm going to use pandas to transform a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv")
    df["Years to 30"] = 30 - df["Age"] # Include a new column in the dataframe that calculates how many years until each student turns 30 years old
    print(df)

    df["Grade"] = df["Grade"]+0.5 # Increase the grade of each student by 0.5
    print(df)
    
    df = df.rename(columns={"Grade": "Grades"}) # Rename the column name 'Grade' into 'Grades'
    print(df.columns)

    df = df.drop(columns=["Career"]) # Delete Career column
    print(df)

    df = df.drop(index=[1]) # Delete the row with index = 1
    print(df)
main()