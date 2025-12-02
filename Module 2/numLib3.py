import time
import numpy as np

my_mat = np.random.rand(5,5)
another_mat = np.random.rand(5,5)
start= time.time()

dot_mut = my_mat.dot(another_mat)
end= time.time()

print("it took {} to calculate dot product! ".format(round(end-start, 4)))