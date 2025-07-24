# Jonatan Paschoal
# 24 de jul de 2025
# Transposição de matrizes em python
# 
#-------------------------------------------

# Biblioteca
import numpy as np

# Matrizes
S = np.array([[1,4,3],[4,2,5],[3,5,0]]) # matriz simétrica
A = np.array([[1,2,3,6],[9,7,4,6]])
B = np.array([[8,5,3,3],[1,0,1,8]])

# Método para transpor matrizes np.transpose(matriz)
ST = np.transpose(S)
AT = np.transpose(A)
BT = np.transpose(B)

# Mostrar matrizes transposta
print('#1 ST = ')
print(ST)
print('#2 AT = ')
print(AT)
print('#3 BT = ')
print(BT)

# Método para transpor matrizes matriz.T
S.T
A.T
B.T
# Mostrar matrizes transposta
print('#4 ST = ')
print(ST)
print('#5 AT = ')
print(AT)
print('6# BT = ')
print(BT)

# Testando propriedade da transposição de matrizes
# i) Simetria de matrizes
x = np.array_equal(S,S.T)
print(x)

# ii) Transposta da transposta
y = np.array_equal(A.T.T, A)
print(y)

# iii) Soma de transposta
z = np.array_equal((A+B).T, A.T+B.T)
print(z)

# iv) transposta de uma matriz multipplicada por um escalar
k = 2
w = np.array_equal((k*B).T, k*(B.T))
print(w)