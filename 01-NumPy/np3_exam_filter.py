# In this project, I'm going to get filtered information from exam dataset

import numpy as np

exams = np.array([2, 7, 6, 8, 3.5, 6, 9.5, 6.75, 4, 5.25, 9])

def main(exams):
    filter_pass = exams >= 5 # Transform exams in a boolean array were passed exams are true
    filter_fail = exams < 5 # Transform exams in a boolean array were failed exams are true
    
    print(exams[filter_pass]) # Print passed exams
    print(exams[filter_fail]) # Print failed exams

    passed_exams = np.sum(filter_pass) # Counts how many exams passed
    failed_exams = np.sum(filter_fail) # Counts how many exams falied
    print(f"Number of passed exams: {passed_exams}")
    print(f"Number of failed exams: {failed_exams}")

    passed_exams_average = np.mean(exams[filter_pass]) # Average of passed exams
    print(f"Average of passed exams: {passed_exams_average}")
main(exams)