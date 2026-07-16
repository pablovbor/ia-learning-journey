# In this project, I'm going to use pandas to explore in a student dataset

import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Charlie", "Pablo", "Eva", "Frank"],
    "Age": [20, 22, 21, 23, 20, 24],
    "Grade": [8.5, 6.2, 9.1, 9.4, 8.0, 5.9],
    "Career": [
        "Computer Science",
        "Mathematics",
        "Physics",
        "Telecommunications",
        "Biology",
        "Mathematics"
    ]
}

def main():
    df = pd.DataFrame(students) # Creating a DataFrame from the students dictionary
    print(df) 

    #rows = df.shape[0] # Getting the number of rows in the DataFrame (6)
    #columns = df.shape[1] # Getting the number of columns in the DataFrame(4)
    rows, columns = df.shape # Same as above, but in one line (6,4)
    print(f"\nNumber of students: {rows} \nNumber of columns {columns}\n")

    print(f"Column names: ") 
    for column in df.columns: # Iterating through the column names of the DataFrame
        print(column) # Printing each column name
    
    avg_age = df["Age"].mean() # Calculating the average age of the students
    print(f"\nAverage age of students: {round(avg_age, 2)}") # Printing

    avg_grade = df["Grade"].mean() # Calculating the average grade of the students
    print(f"Average grade of students: {round(avg_grade, 2)}") # Printing

    print("\nData types of each column:")
    for column in df.columns:
        print(f"{column}: {df[column].dtype}") # Printing the data type of each column
main()