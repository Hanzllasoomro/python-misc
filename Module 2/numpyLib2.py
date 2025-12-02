import numpy as np

# linear algebra
import numpy.linalg as la

my_mat = np.array([[1,2], [3,4]])
# calculate determinant
det = la.det(my_mat)
# calculate inverse of a matrix. Inv = adj(matrix)/det(matrix). NOTE: Make sure its not SINGULAR!
inverse_mat = la.inv(my_mat)
# calculate eigen values. NOTE: make sure the matrix is SQUARE [eigen values do not exit for matrix whose dimensions are mxn where m!=n]!
eig_values, eig_vectors = la.eig(my_mat)
# calculate cholesky factorization. NOTE: make sure matrix is Positive Definite!
cholesky = la.cholesky(np.array([[7,2], [2,1]]))
# calculate rank of a matrix. Rank of a matrix is the number of linearly independent columns/rows in a matrix.
rank = la.matrix_rank(my_mat)

print("my_mat: ", my_mat)
print("la.matrix_rank(my_mat): ",la.matrix_rank(my_mat))
print("cholesky",cholesky)
print("rank",rank)
print("la.matrix_rank(inverse_mat)",la.matrix_rank(inverse_mat))
print("la.matrix_rank(cholesky)",la.matrix_rank(cholesky))
print("la.matrix_rank(rank)",la.matrix_rank(rank))
print("det", det)