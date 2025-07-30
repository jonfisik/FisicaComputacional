# Jonatan Paschoal
# 30 de jul de 2025
# Determinante de matrizes em python
# Determinates - numpy.linalg, função para uso do (det)
#
#-------------------------------------------
# Determinantes

import numpy as np
from numpy.linalg import det

A = np.array([[1,2,4],[5,3,-1],[7,2,0]])
print('\n',A)

print('Det_A = ',det(A))

#---------------------------------------------

B = np.array([[1,2,4,5,6,7],[5,3,-1,5,1,2],[7,2,0,1,4,9],[1,2,1,5,6,5],[-7,2,4,-1,6,6],[0,2,5,5,9,7]])
print('Dimensão da matriz B', B.shape)
print('Det_B = ',det(B))