"""
a. Write a simple MPI script mpi_ranks.py that prints the rank of the different processes when running
$ mpirun python mpi_ranks_day3.py
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(rank)