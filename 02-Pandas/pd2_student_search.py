# In this project, I'm going to use pandas to explore in a student dataset

import pandas as pd

def main():
    df = pd.read_csv("datasets/students.csv") # Reading the CSV file (dataset) into a DataFrame
    print(df) # Printing the DataFrame

    print(df["Name"]) # Printing the "Name" column of the DataFrame
    print(df["Age"]) # Printing the "Age" column of the DataFrame
    print(df["Grade"]) # Printing the "Grade" column of the DataFrame
    print(df["Career"]) # Printing the "Career" column of the DataFrame

    name_and_grade = df[["Name", "Grade"]] # Selecting the "Name" and "Grade" columns from the DataFrame
    print(name_and_grade)

    print("\nUsing .iloc to select rows by index:")
    first_student = df.iloc[0] # Selecting the first row of the DataFrame
    print(first_student)
    first_3_students = df.iloc[0:3] # Selecting the first 3 rows of the DataFrame
    print(first_3_students)
    last_2_students = df.iloc[-2:] # Selecting the last 2 rows of the DataFrame
    print(last_2_students)

    print("\nUsing .loc to select rows by index:")
    first_student_loc = df.loc[0] # Selecting the first row of the DataFrame using .loc
    print(first_student_loc)
    third_student_loc = df.loc[2] # Selecting the third row of the DataFrame using .loc
    print(third_student_loc)
    
    print("\nSelecting data using .loc")
    alice_name = df.loc[0,"Name"] # Selecting the name of the first student using .loc
    print(alice_name)
    pablo_age = df.loc[3,"Age"] # Selecting the age of the fourth student using .loc
    print(pablo_age)
    eva_career = df.loc[4,"Career"] # Selecting the career of the fifth student using .loc
    print(eva_career)
main()