import numpy as np
import itertools
def inpt_size():
  while True:
    try:
        x = int(input('Enter the size of square matrix'))
        if x>=1:
           return x
        else:
           inpt_size()
    except ValueError:
        print("Enter num")
def random_matrix(dim):
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix
def permutations(matrix):
    t = list(itertools.permutations(range(len(matrix))))
    return t
#def determinant uncomplete
matrix = random_matrix(inpt_size())
permutations(matrix)
print(matrix)