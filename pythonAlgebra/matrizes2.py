# Jonatan Paschoal
# 22 de jul de 2025
# Tippos de matrizes em python
# 
#-------------------------------------------

# Biblioteca
import numpy as np

# Matrizes Linha

L1 = np.array([3,4,5])
print('Matrizes linha')
print('L1 = ')
print(L1)
print('')

L2 = np.array([[3,4,6]]) 
print('L2 = ')
print(L2)
print('')

L3 = np.array([[0,0,0,0]])
print('L3 = ')
print(L3)
print('')

# Matrizes Coluna
# Cada colchete é uma linha,
# cada casa depois da virgula uma coluna.
C1 = np.array([[1],[3],[7]]) 
print('C1 = ')
print(C1)
print('')

# Matriz nula
N = np.zeros([2,2]) # função zeros
print('N = ')
print(N)
print('')

N1 = np.zeros((2,2)) # paranteses
print('N1 = ')
print(N1)
print('')

N2 = np.zeros([5,5]) # colchetes
print('N2 = ')
print(N2)
print('')

# Matriz diagonal
D = np.diag([1,2,3,6,5]) # elementos da diagonal principal
print('D = ')
print(D)
print('')

E = np.diag([1,1,1,1]) # Matriz identidade
print('E = ')
print(E)
print('')

# Matriz identidade
I = np.eye(4,4)
print('I = ')
print(I)
print('')

# matriz.shape(n_linhas, n_colunas)
print('L1',L1.shape)
print('L2',L2.shape)
print('L3',L3.shape)
print('C1',C1.shape)
print('N ',N.shape)
print('N1',N1.shape)
print('N2',N2.shape)
print('D ',D.shape)
print('E ',E.shape)
print('I ',I.shape)
print('')