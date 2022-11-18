import numpy as np


B = np.array([[5, 6], [7, 8]])
A = np.array([[3, -1], [5, -2]])
C = np.array([[14, 16], [9, 10]])

b = np.linalg.inv(B)
a = np.linalg.inv(A)

print(b)
print(a)
print(a @ C @ b )
print(np.sum(a @ C @ b))