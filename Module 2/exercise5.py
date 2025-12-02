# Numpy Module
#  EXERCISE – 5
# • Write a NumPy program to extract upper triangular part of a NumPy
# matrix
#  • Write a NumPy program to extract all the elements of the second and
# third columns from a given (4x4) my_array
#  • Write a NumPy program to count the occurrence of a specified item
# in a given NumPy my_array
#  • Write a NumPy program to sum and compute the product of a NumPy
# my_array elements

import numpy as np

# Sample 4x4 matrix
my_matrix = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

# Extract upper triangular part
upper_tri = np.triu(my_matrix)

print("Upper Triangular Part:\n", upper_tri)
# Using the same matrix
# Extract second and third columns (index 1 and 2)
columns_2_and_3 = my_matrix[:, 1:3]

print("Second and Third Columns:\n", columns_2_and_3)
# Specify item to count
item = 10

# Count occurrence
count = np.count_nonzero(my_matrix == item)

print(f"Number of occurrences of {item}: {count}")
# Sum of elements
total_sum = np.sum(my_matrix)

# Product of all elements
total_product = np.prod(my_matrix)

print("Sum of elements:", total_sum)
print("Product of elements:", total_product)
