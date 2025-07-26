# Jonatan Paschoal
# 26 de jul de 2025
# Indexação (e slicing) de matrizes em python
# 
#-------------------------------------------
# Slicing de matrizes - indexação de matrizes - parte 2

import numpy as np

A = np.array([[2,3,7,1],[8,6,9,3],[6,9,3,2],[4,3,7,5]])
print('A = \n',A)
print('dim_A = ',A.shape)

print('Linha 3 colunas 2, 3 e 4 - [2,1:4] \n',A[2,1:4])

'''
Indexação (dos índices) python
A = [A00, A01, A02, A03,
	 A10, A11, A12, A13,
	 A20, A21, A22, A23,
	 A30, A31, A31, A33]
'''