import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array to a 2D array with 2 rows and 3 columns
reshaped_arr = arr.reshape(1, -1)

print("Original Array:")
print(arr)
print(arr.shape)
print("\nReshaped Array:")
print(reshaped_arr)
