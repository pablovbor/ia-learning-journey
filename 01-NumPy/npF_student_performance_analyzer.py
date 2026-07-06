# This is the final project of NumPy, the project consists in create a system that analyze and create a dataset of students performance.
# info in dataset: [age, exam1, exam2, exam3, attendance]

import numpy as np

# 1. Dataset generation
students_number = np.random.randint(10, 31)
age = np.random.randint(18, 31, size=students_number)
exam1 = np.random.randint(0, 11, size=students_number)
exam2 = np.random.randint(0, 11, size=students_number)
exam3 = np.random.randint(0, 11, size=students_number)
attendance = np.random.randint(50, 101, size=students_number)

def main():
    # 2. Basic information about the dataset
    dataset = np.vstack((age, exam1, exam2, exam3, attendance)).T  # Combining the data into a dataset and transposing to get a shape of (students, 5)
    print(dataset)
    print(f"Number of students: {students_number}")
    print(f"Dataset shape: {dataset.shape}")  # Print the shape of the dataset (students_number, 5)
    print(f"Dataset dimensions: {dataset.ndim}\n")  # Print the number of dimensions of the dataset (2)

    # 3. Statistical information about exams
    print(f"Mean of exam1: {round(dataset[:, 1].mean(), 2)}")  # Mean of exam1 scores
    print(f"Max score of exam1: {dataset[:, 1].max()}")  # Max score of exam1 scores
    print(f"Min score of exam1: {dataset[:, 1].min()}\n")  # Min score of exam1 scores
    print(f"Mean of exam2: {round(dataset[:, 2].mean(), 2)}")  # Mean of exam2 scores
    print(f"Max score of exam2: {dataset[:, 2].max()}")  # Max score of exam2 scores
    print(f"Min score of exam2: {dataset[:, 2].min()}\n")  # Min score of exam2 scores
    print(f"Mean of exam3: {round(dataset[:, 3].mean(), 2)}")  # Mean of exam3 scores
    print(f"Max score of exam3: {dataset[:, 3].max()}")  # Max score of exam3 scores
    print(f"Min score of exam3: {dataset[:, 3].min()}\n")  # Min score of exam3 scores

    print(f"Global mean of exams: {round(dataset[:, 1:4].mean(), 2)}")  # Mean of all exam scores
    print(f"Median of all exams: {np.median(dataset[:, 1:4])}")  # Median of all exam scores
    print(f"Standard deviation of all exams: {round(np.std(dataset[:, 1:4]), 2)}")  # Standard deviation of all exam scores
    print(f"75th percentile of all exams: {np.percentile(dataset[:, 1:4], 75)}")  # 75th percentile of all exam scores

    # 4. Final score ponderation
    weights = np.array([0.3, 0.3, 0.4])  # Weights for exam1, exam2, and exam3
    final_scores = np.dot(dataset[:, 1:4], weights)  # Calculate final scores using dot product
    print(f"\nFinal scores: {final_scores}")

    # 5. Add final scores to the dataset
    dataset = np.column_stack((dataset, final_scores))  # Add final scores as a new column to the dataset
    print(f"\nUpdated dataset with final scores:\n{dataset}")

    # 6. Filter students
    passed_filter = dataset[dataset[:, 5] >= 5]  # Filter students who passed (final score >= 5)
    failed_filter = dataset[dataset[:, 5] < 5]  # Filter students
    excellent_filter = dataset[(dataset[:, 5] >= 8) & (dataset[:, 4] >= 80)]  # Filter students who excelled (final score >= 8 and attendance >= 80)
    print(f"\nStudents who passed:\n{passed_filter}")
    print(f"\nStudents who failed:\n{failed_filter}")   
    print(f"\nStudents who excelled:\n{excellent_filter}")

    # 7. Ranking
    best_student = dataset[np.argmax(dataset[:, 5])]  # Get the student with the highest final score
    worst_student = dataset[np.argmin(dataset[:, 5])]  # Get the student with the lowest final score
    print(f"\nBest student:\n{best_student}")
    print(f"\nWorst student:\n{worst_student}")
    top_3_students = dataset[np.argsort(dataset[:, 5])[-3:][::-1]]  # Get the top 3 students based on final scores 
    print(f"\nTop 3 students:\n{top_3_students}")

    # 8. Student performance report
    print(f"\n======== STUDENT PERFORMANCE REPORT ========")
    print(f"Total number of students: {students_number}")
    print(f"Average final score: {round(final_scores.mean(), 2)}")
    print(f"Median final score: {np.median(final_scores)}")
    print(f"Standard deviation of final scores: {round(np.std(final_scores), 2)}")
    print(f"Number of students who passed: {len(passed_filter)}")
    print(f"Number of students who failed: {len(failed_filter)}")
    print(f"Number of students who excelled: {len(excellent_filter)}")
    print(f"Average attendance: {round(dataset[:, 4].mean(), 2)}")
    print(f"Best student: {best_student}")
    print(f"Worst student: {worst_student}")

main()









