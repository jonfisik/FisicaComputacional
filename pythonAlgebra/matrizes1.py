# Jonatan Paschoal
# 20 de jul de 2025
# Formas de matrizes em python
# 
#-------------------------------------------

# Biblioteca
import numpy as np

# Matrizes - np.array(x,y)

# Matriz 2 x 2
A = np.array([[2,-1],[0,4]])
print('A = ')
print(A)
print('')

# Matriz 2 x 3
B = np.array([[1,0,-4],[4,-3,2]])
print('B = ')
print(B)
print('')

# Matrizes - representação 2 (função np.matrix())
C = np.matrix('1 2; 3 4')
print('C = ')
print(C)
print('')

D = np.matrix([[1,2],[3,4]])
print('D = ')
print(D)
print('')

print(type(A))
print(type(B))
print(type(C))
print(type(D))
print('')