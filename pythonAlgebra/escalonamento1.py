# Jonatan Paschoal
# 26 de jul de 2025
# Escalonamento de matrizes em python
# 
#-------------------------------------------
# Escalonamento de matrizes


import numpy as np

M = np.array([[1,4,3,1],[2,5,4,4],[1,-3,-2,5]])
print(M)

M[1,:] = -2*M[0,:] + M[1,:]
print(M)

M[2,:] = -1*M[0,:] + M[2,:]
print(M)

M[1,:] = -1/3*M[1,:]
print(M)

M[0,:] = -4*M[1,:] + M[0,:]
print(M)

M[2,:] = 7*M[1,:] + M[2,:]
print(M)

M[2,:] = -3*M[2,:]
print(M)

M[1,:] = -1/3*M[2,:] + M[1,:]
print(M)

M[0,:] = -1/3*M[2,:] + M[0,:]
print(M)

M[2,:] = M[2,:]/3
print(M)

M[1,:] = 5*M[2,:] + M[1,:]
print(M)