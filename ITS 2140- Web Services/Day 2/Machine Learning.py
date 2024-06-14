#NumPy
import numpy as np

# Create an array
a = np.array([1, 2, 3, 4])

# Perform basic operations
print(a + 2)  # Add 2 to each element: [3, 4, 5, 6]
print(a * 3)  # Multiply each element by 3: [3, 6, 9, 12]

# Create a 2D array
b = np.array([[1, 2], [3, 4]])

# Matrix multiplication
c = np.dot(a, b)

print(c)