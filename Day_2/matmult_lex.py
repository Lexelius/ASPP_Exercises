"""
%timeit %run '/Users/lexelius/Documents/PhD/Courses/Advanced_Scientific_Python_Programming/day2-bestpractices-1/matmult.py'
4.04 s ± 16.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit %run '/Users/lexelius/Documents/PhD/Courses/Advanced_Scientific_Python_Programming/day2-bestpractices-1/matmult_lex.py'
"""
# Program to multiply two matrices using nested loops
import random
import numpy as np
import line_profiler

N = 250

# NxN matrix
#@profile
def matmultiply(N):
    X = np.round(np.random.random(N*N)*100).reshape((N,N))

    # Nx(N+1) matrix
    Y = np.round(np.random.random(N*N)*100).reshape((N,N))
    return np.dot(X,Y)

result = matmultiply(N)
# for r in result:
#     print(r)

"""
a. Investigate the performance of the matmult.py script
In which line(s) of the script would you start optimizing for speed?
    Ans: Line 9 and 14 ( X.append([random.randint(0,100) for r in range(N)]) ).

b. Investigate the performance of the euler72.py script
In which line(s) of the script would you start optimizing for speed? (This is one problem from the euler project: https://projecteuler.net/problem=72)
    Ans: Line 26, however I'd probably start looking into if it's possible to rewrite the factorize function so that n could be an array instead of using loops.

c. Improve the performance of the matmult.py script
What is the best performance that you achieved with N=250?
"""