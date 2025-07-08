import numpy as np

mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('The shape of mat is:', mat.shape)
# it can be reshaped to any shape that is consistent with the data size
new_mat = mat.reshape(1,9)
print('The shape of new_mat is:', new_mat.shape)
# you can try transposing it as well.
trans_new_mat = new_mat.T
print('The transposed shape of new_mat is:', trans_new_mat.shape)

# you can create diagonal matrices, identity matrices
diag = np.diag([1,2,3,4])
identity = np.identity(10) # creates a 10 x 10 matrix with ones at diagonals and rest zeros

# you can create arrays of random numbers or sequences
seq = np.arange(start=0, stop=100, step=5) # creates an array starting from 0, with a step size of 5 till 100. [0,5,10,....,90,95]
# If you only pass np.random.rand(10), it creates a 1D vector of length 10
rands_1d = np.random.rand(10)
rands_2d = np.random.rand(10, 10) # creates 10x10 matrix with random numbers.


# you can find min and max and min as well as the index of max number or min number
my_array = np.array([1,3,5,7,23,6,2,31,5])
print('The max is {} at index {}'.format(my_array.max(), my_array.argmax()))
print('The min is {} at index {}'.format(my_array.min(), my_array.argmin()))

import time
# you can perform dot products of matrices in a matter of seconds
my_mat = np.random.rand(1000, 1000)
another_mat = np.random.rand(1000, 1000)
start = time.time()
# make sure the dimensions agree!
dot_mul = my_mat.dot(another_mat)
end = time.time()
print('It took {} seconds to calculate dot product!'.format(round(end-start, 4)))

start = time.time()
prod = my_mat * another_mat
end = time.time()
print('It took {} seconds to calculate dot product!'.format(round(end-start, 4)))

