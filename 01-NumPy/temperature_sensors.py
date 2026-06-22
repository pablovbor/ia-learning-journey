# In this project , Im going to simulate a temperature sensor dataset, then im going to get maximum, minimum, average temperature and how many times the temperature was above 25 degrees.

import numpy as np

temperatures = np.random.randint(
    low=15, high=30, size=24) # Simulate a week's worth of hourly temperature data

def main():
    print(temperatures) # Print the simulated temperature data
    print("Maximum Temperature:", temperatures.max()) # Get the maximum temperature
    print("Minimum Temperature:", temperatures.min()) # Get the minimum temperature
    print("Average Temperature:", temperatures.mean()) # Get the average temperature
    print("Number of times temperature was above 25 degrees:", np.sum(temperatures > 25)) # Count how many times the temperature was above 25 degrees
main()