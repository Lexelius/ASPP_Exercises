import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
null = np.zeros(10)
null[4] = 1

# b. Create a vector with values ranging from 10 to 49
B = np.arange(10, 50)

# c. Reverse a vector (first element becomes last)
C = B[::-1] # a view of the reversed B-vector

# d. Create a 3x3 matrix with values ranging from 0 to 8
D = np.arange(0, 9).reshape((3, 3))

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
E = [1, 2, 0, 0, 4, 0]
nonz_ind = np.where(np.array(E) != 0)[0]

# f. Create a random vector of size 30 and find the mean value
F = np.random.random(30)
Fmean = F.mean()

# g. Create a 2d array with 1 on the border and 0 inside
Gshape = [5, 6]
## solutions 1, starting with zeros
G1 = np.pad(np.zeros((Gshape[0]-2, Gshape[1]-2)), 1, constant_values=1) # 22 µs ± 37.2 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
## solution2, starting with ones
G2 = np.ones((Gshape[0], Gshape[1]))
G2[1:-1, 1:-1] = 0 # 2.11 µs ± 8.92 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
H = np.zeros((8, 8))
H[::2, ::2] = 1
H[1::2, 1::2] = 1
## Or as a one-liner not dependent on nr of dimensions:
## H = np.indices((8,8).sum(axis=0) % 2

# i. Create a checkerboard 8x8 matrix using the tile function
I = np.array([[0, 1], [1, 0]])
I = np.tile(I, (4, 4))

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[3:8] = -Z[3:8]
print(Z)

# k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z.sort()
print(Z)

# l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = A == B
print(equal)

# m. How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.view('float32')
print(Z.dtype)

# n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3, 3)
B = A + 1
C = np.dot(A, B)
D = C[:len(C)].flat[0::len(C)+1]
print(D)

