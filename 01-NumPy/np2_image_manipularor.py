# In this project, Im going manipulate a 10x10 pixel image with values between 0 (dark) and 255 (light)

import numpy as np

image = np.random.randint(low = 0, high = 256, size = (10, 10))

def main(image):
    
    print(f"Original image:\n {image}") # Prints the image
    image += 50 # Bright increase
    image = np.clip(image, 0, 255) # Values below 0 = 0, Values up to 255 = 255
    print(f"\nManipulated image:\n {image}") # Prints the image with brigth filter
    
main(image) # Pass the image as an argument to avoid modifying global variables
