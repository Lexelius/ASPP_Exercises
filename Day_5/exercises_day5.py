import numpy as np
from scipy import linalg
#%% 1. Scipy

#A = np.arange(1, 10).reshape((3, 3))  # scipy.arange(..) is deprecated
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1., 2., 3.])

# A = np.asmatrix(np.arange(1, 10).reshape((3, 3))) # scipy.arange(..) is deprecated
# b = np.asmatrix(np.array([1, 2, 3])).T

try:
    # c. Solve the linear system of equations A x = b
    x = linalg.solve(A, b)

    # d. Check that your solution is correct by plugging it into the equation
    sol = np.dot(A, x)
    (sol == b).all()
except np.linalg.LinAlgError as err:
    print('Error: ', err)

# e. Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)
try:
    B = np.random.random((3, 3))
    X = linalg.solve(A, B)
    solB = np.dot(A, X)
    (solB == B).all()
except np.linalg.LinAlgError as err:
    print('Error: ', err)


# f. Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eig_val, eig_vec = linalg.eig(A)
print('Eigen values: \n', eig_val)
print('Eigen vectors: \n', eig_vec)


# g. Calculate the inverse, determinant of A
try:
    inv = linalg.inv(A)
except np.linalg.LinAlgError as err:
    print('Error: ', err)
det = linalg.det(A)

# h. Calculate the norm of A with different orders
norm1 = linalg.norm(A, 1)
norm2 = linalg.norm(A, 2)

