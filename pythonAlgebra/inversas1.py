# Jonatan Paschoal
# 03 de ago de 2025
# Matrizes inversas em python (inv)
#
#-------------------------------------------
# Matrizes Inversas


import numpy as np
from numpy.linalg import det, inv

# Matrize A
A = np.array([[1,-7,2],[4,2,7],[1,4,-1]])

# print
print('Matriz A = \n', A)

# det(A) é diferente de zero
print('\ndet(A) =', det(A))

# Inversa de A
inv_A = inv(A)
print('\nInversa da matriz A \n', inv_A)
print('\nA x inv_A = \n', A.dot(inv_A))

# Matriz B
# Matriz B não admite inversa. B é uma matriz singular.
B = np.array([[1,1,2],[1,1,2],[3,-1,-1]])

# print
print('\nMatriz B = \n', B)

# det(B) é igual a zero
print('\ndet(B) =', det(B))
print('Matriz B não admite inversa.')