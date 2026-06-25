# In this project, I'm going to filter extreme temperatures from a temperature dataset

import numpy as np
temperatures = np.random.randint(-10, 41, size=30)

def main():
    print(temperatures) 
    # Filters
    extreme_cold_filter = temperatures < 0
    extreme_hot_filter = temperatures > 30
    hot_filter = temperatures > 20

    # Temperatures
    extreme_cold = temperatures[extreme_cold_filter]
    extreme_hot = temperatures[extreme_hot_filter]
    hot = temperatures[hot_filter]

    # Counters
    extreme_cold_days_counter = np.sum(extreme_cold_filter)
    extreme_hot_days_counter = np.sum(extreme_hot_filter)
    hot_days = np.sum(hot_filter)

    print(f"Extreme cold days: {extreme_cold_days_counter}\nTemperatures:{extreme_cold}\n")
    print(f"Extreme hot days: {extreme_hot_days_counter}\nTemperatures {extreme_hot}\n")

    # Average hot temperatures
    average_hot_days = np.sum(temperatures[hot_filter])/hot_days
    print(f"Average temperature of hot days: {average_hot_days}")

    # Max and min temperatures
    max_temperature = np.max(temperatures)
    min_temperature = np.min(temperatures)
    print(f"Maximum temperature: {max_temperature}")
    print(f"Minimum temperature: {min_temperature}")
main()