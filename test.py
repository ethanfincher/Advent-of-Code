import numpy as np

# Example 1D array and 2D array
array_1d = np.array([1, 2, 4])
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Check if the 1D array matches any row in the 2D array
matches = np.any(np.all(array_2d == array_1d, axis=1))
print(matches)