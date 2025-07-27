# Jonatan Paschoal
# 27 de jul de 2025
# Operações com matrizes
#
#-------------------------------------------
# Operações com matrizes

import numpy as np

A = np.array([[2,4,6],
			 [1,2,7],
			 [3,2,9]], dtype=float)

B = np.array([[-1,4,5],
			 [6,3,1]], dtype=float)

C = np.array([[0,4,3],
			 [1,-3,-1],
			 [3,1,2]], dtype=float)

print('dim_A = \n',A.shape)
print('dim_B = \n',B.shape)
print('dim_C = \n',C.shape)

# Soma de matrizes - mesma dimensão
S = A + C
print('S_AC = \n',S)

# Soma de linha (SL)
SL = A[0,:] + B[0,:]
print('SL = ',SL)

# Subtração de matrizes
SUB_AC = A- C
print('SUB_AC = \n',SUB_AC)

# Multiplicação B(2x3) * A(3x3)
M = B.dot(A)
print('M_BC = \n',M)


# Divisão de matrizes
D = A/C
print('D = \n',D)


# Multiplicação por um escalar
k = 2
print(f'Multiplicação por escalar, {k} x A = \n',k*A)

# Validando multiplicação
M_AC = A.dot(C)
print('M_AC =\n', M_AC)

#
a11 = A[0,:].dot(C[:,0])
print('a11 = ',a11)
#
a12 = A[0,:].dot(C[:,1])
print('a11 = ',a11)
#
a13 = A[0,:].dot(C[:,2])
print('a13 = ',a13)

#M_CA = C.dot(A)
#print('M_AC =\n', M_CA)

