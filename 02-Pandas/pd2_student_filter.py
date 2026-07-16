# In this project, I'm going to use pandas to explore in a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv") # Reading the CSV file (dataset) into a DataFrame

    older_21 = df.loc[df["Age"] > 21] # Filtering the DataFrame to get students older than 21
    print(older_21) # Printing the filtered DataFrame
    greater_than_8 = df.loc[df["Grade"] > 8] # Filtering the DataFrame to get students with grades greater than 8
    print(greater_than_8) # Printing the filtered DataFrame

    older_and_greater = df.loc[(df["Age"] > 21) & (df["Grade"] > 8)] # Filtering the DataFrame to get students older than 21 and with grades greater than 8
    print(older_and_greater) # Printing the filtered DataFrame

    older_or_greater = df.loc[(df["Age"] > 21) | (df["Grade"] > 8)] # Filtering the DataFrame to get students older than 21 or with grades greater than 8
    print(older_or_greater) # Printing the filtered DataFrame

    math_or_biology = df.loc[df["Career"].isin(["Mathematics", "Biology"])] # Filtering the DataFrame to get students whose subject is either Math or Biology usinf .isin()
    print(math_or_biology) # Printing the filtered DataFrame
main()