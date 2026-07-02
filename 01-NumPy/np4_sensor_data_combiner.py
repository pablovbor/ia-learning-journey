# In this project, I'm going to combine sensor data using NumPy

import numpy as np

sensor1 = np.random.randint(0, 100, size = 10)  # Simulating sensor 1 data with random integers
sensor2 = np.random.randint(0, 100, size = 10)  # Simulating sensor 2 data with random integers
sensor3 = np.random.randint(0, 100, size=10)

def main():
    print(sensor1)
    print(sensor2)

    combined = np.vstack((sensor1, sensor2))  # Combining the two sensor data arrays vertically
    print(combined)
    print(combined.shape)  # Print the shape of the combined array (2,10)

    combined_horizontal = np.hstack((sensor1, sensor2))  # Combining the two sensor data arrays horizontally
    print(combined_horizontal)
    print(combined_horizontal.shape)  # Print the shape of the horizontally combined array (20,)

    transposed = combined.T  # Transposing the combined array
    print(transposed)
    print(transposed.shape)  # Print the shape of the transposed array (10,2)

    dataset = np.vstack((sensor1, sensor2, sensor3)).T  # Combining three sensor data arrays and transposing to get a shape of (10,3)
    print(dataset)
    print(dataset.shape)  # Print the shape of the dataset (10,3)
main()