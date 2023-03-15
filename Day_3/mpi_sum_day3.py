"""
b. Write a small script mpi_sum.py which calculates the sum over all
ranks and prints the result from the process with rank 0.
"""
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
rsize = comm.Get_size()

arr = np.arange(20)
solution = np.sum(arr)

# Designate chunks of the array to each rank
ind0 = (len(arr)//rsize) * rank
if rank == rsize-1:
    ind1 = (len(arr) // rsize) * (rank + 1) + len(arr)%rsize
else:
    ind1 = (len(arr)//rsize) * (rank+1)
#print(f'rank {rank}, ind {ind0}:{ind1}, arr[{ind0}:{ind1}] {arr[ind0:ind1]}')

# Sum each chunk within each rank
arrsum_rank = np.sum(arr[ind0:ind1])
#print(rank, arrsum_rank)
# Gather all the sums to rank 0
arrsum_all = comm.gather(arrsum_rank, root=0)
# Sum the sums from all ranks
if rank == 0:
    arrsum = np.sum(arrsum_all)
    print('Sum of array is: {arrsum}')
    assert arrsum == solution

