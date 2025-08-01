# Jonatan Paschoal
# 31 de jul de 2025
# Determinante de matrizes em python
# Determinates - numpy.linalg, função para uso do (det)
#
#-------------------------------------------
# Determinantes propriedades


import numpy as np
from numpy.linalg import det

# Matriz
A = np.array(([1,2,4],[5,3,-1],[7,2,0]))
print(f'A = \n',A)

Az = np.zeros([3,3])
print('Az = \n',Az)

# 1) det(Az) = 0
print('\ndet(Az) = ',det(Az))

# 2) det(A) = det(A.T)
print(f'\ndet(A) = {det(A)}, det(aT) = {det(A.T)}.')
print('\ndet(A) = det(A.T), ',det(A) == det(A.T))

# 3) # Se B = k*A[0,:], det(B) = k*det(A)
k = 3
B = A.copy()
B[0,:] = k*B[0,:]
print(f'\nB = {k}xA = \n',B)
print('\ndet(B) = ',det(B))
print(f'det({k} x A) = ',k*det(A))
print('det(B) = k x det(A) = ',det(B) == k*det(A))

# 4) Se trocarmos a posição de duas linhas o det muda de sinal
L1 = A[0,:] # linha 1
L2 = A[1,:] # linha 2
L3 = A[2,:] # linha 3

C = np.array([L2,L1,L3])
print('C = \n',C)
print('det(C) = \n',det(C))
print('det(A) = \n',det(A))

# 5) Matrizes com duas linhas iguais -> det = 0
D = np.array([L1,L1,L2])
print('D = \n',D)
print('det(C) =\n',det(D))

# 6) det(A+B) != det(A) + det(B)
A = np.array(([1,2,4],[5,3,-1],[7,2,0]))
B = np.array(([0,5,4],[8,2,1],[9,-2,3]))
np.array_equal(det(A+B),det(A)+det(B))
print('Det(a+B)\n',det(A+B))
print('det(A) + det(B) = \n',det(A) + det(B))

# 7) det(A.dot(B)) = det(A)*det(B)
print('det(Ax(B) = \n',det(A.dot(B)))
print('det(A)xdet(B)',det(A)*det(B))
