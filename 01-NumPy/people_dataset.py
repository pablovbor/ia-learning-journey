# In this project, Im going to representate people's data [age, height, weight] using numpy arrays and get all ages from data, all heights from data, add 2cm to all heights
# and get the weightest person's data from the dataset.

import random
import numpy as np

people = random.randint(1,10) # Randomly generate the number of people between 1 and 10
age = np.random.randint(low=18, high=70, size=people) # Randomly generate ages between 18 and 70 for the number of people
height = np.random.randint(low=150, high=200, size=people) # Randomly generate heights between 150 and 200 cm for the number of people
weight = np.random.randint(low=50, high=100, size=people) # Randomly generate weights between 50 and 100 kg for the number of people
data = np.column_stack((age, height, weight)) # Create a numpy array to hold all the data, np.array([age, height, weight]) it would create a 1D array, 
                                              # but we want a 2D array, so we use np.column_stack to stack the arrays as columns.

def main():
    print(data) #Print all the data
    print("All ages from data:", data[:, 0]) #Print all ages from data, IMPORTANT([:, 0] means all rows and first column, if it were [0, :] it would mean first row and all columns)
    print("All heights from data:", data[:, 1]) #Print all heights from data
    data[:, 1] += 2 #Add 2cm to all heights
    print("All heights after adding 2cm:", data[:, 1]) #Print all heights
    weightest_person_index = np.argmax(data[:, 2]) #Get the index of the weightest person
    weightest_person_data = data[weightest_person_index, :] #Get the data of the weightest person
    print("Weightest person's data [age, height, weight]:", weightest_person_data) #Print the data of the weightest person
main()

