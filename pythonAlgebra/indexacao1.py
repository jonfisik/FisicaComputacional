# Jonatan Paschoal
# 24 de jul de 2025
# Indexação (slicing) de matrizes em python
# 
#-------------------------------------------
# Slicing de matrizes - indexação de matrizes - parte 1

import numpy as np

A = np.array([[2,4,6],[4,7,1],[9,3,8]])
print('A =\n', A)

# Retorna a dimensão da matriz
DIM_A = A.shape
print('DIM_A = \n', DIM_A)

# Slicing - fatiamento
print('Toda matriz [:]\n',A[:])

# linha 1 e todas as colunas
print('Linha 1 e todas as colunas [1,:]\n',A[1,:])

# linha 2 e todas as colunas
print('Linha 2 e todas as colunas [1,:]\n',A[2,:])

# Coluna 0 e todas as linhas
print('Coluna 0 e todas as linhas [:,0]\n',A[:,0])

# Um elemento, linha 1 coluna 1
print('Um elemento, linha 1 coluna 1 [1,1]\n',A[1,1])

# J é uma referência de A e não uma cópia
J = A
print('J = A, então J = \n',J)

# Alterar valor da matriz J
J[0,2] = 19
print('J[0,2], novo J = \n',J)

# A matriz A tbm é alterada
print('A matriz A tbm é alterada, A = \n',A)

# Cópia de matrizes
G = J.copy()
print('Cópia das matrizes A e J, G =\n',G)
G[2,2] = 63
print('\n G[2,2] = 63', G)
print('\n Desta vez não altera a matriz A.')
