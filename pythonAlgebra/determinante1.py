# Jonatan Paschoal
# 30 de jul de 2025
# Determinante de matrizes em python
# 
#-------------------------------------------
# Determinantes

import numpy as np

# Matriz A
A = np.array([[1,2,4],[5,3,-1],[7,2,0]])
print('A = \n',A)

# Determinate A
det_A = np.linalg.det(A)
print('Det(A) = \n',np.round(det_A))

# Matriz B
B = np.array([[1, 2], [3, 4]])
print('B = \n',B)

# Determinate
det_B = np.linalg.det(B)
print('Det(B) = \n',np.round(det_B))
