# Python Program to Add Two Matrices
import numpy as np
mat_1 = np.array((
    (1,2,3),
    (4,5,6),
    (7,8,9)
))
mat_2 = np.array((
    (0,1,0),
    (1,0,1),
    (0,1,0)
))
mat_sum = mat_1 + mat_2
print(mat_sum)