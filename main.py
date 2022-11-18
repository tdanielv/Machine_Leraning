import numpy as np
from scipy import sparse
from sklearn import datasets

matrix = np.array([[7, 8, 5, 5, 3], [10, 11, 6, 7, 5], [5, 3, 6, 2, 5], [6, 7, 5, 4, 2], [7, 10, 7, 5, 0]])

print(np.linalg.det(matrix))