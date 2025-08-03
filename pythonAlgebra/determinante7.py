# Jonatan Paschoal
# 02 de ago de 2025
# Determinante de matrizes em python
# Determinates - numpy.linalg, função para uso do (det)
# Funções reutilizáveis e separadores visuais
#-------------------------------------------
# Determinantes propriedades

import numpy as np
from numpy.linalg import det

# Matriz base
A = np.array([[1, 2, 4],
			  [5, 3, -1],
			  [7, 2, 0]])

print("========== MATRIZ A ==========")
print('A =\n', A)

# Propriedade 1: Determinante da matriz nula é zero
Az = np.zeros((3, 3))
print("\n========== 1) det(0) = 0 ==========")
print('Matriz nula Az =\n', Az)
print('det(Az) =', det(Az))

# Propriedade 2: det(A) = det(A transposta)
print("\n========== 2) det(A) = det(A.T) ==========")
print('A.T =\n', A.T)
print(f'det(A) = {det(A):.2f}')
print(f'det(A.T) = {det(A.T):.2f}')
print('Verificação: det(A) == det(A.T)? - ', np.isclose(det(A), det(A.T)))

# Propriedade 3: multiplicar uma linha por escalar k => det é multiplicado por k
print("\n========== 3) Multiplicação de linha por escalar ==========")
k = 3
B = A.copy()
B[0, :] = k * A[0, :]
print(f'B = A com linha 1 multiplicada por {k}:\n', B)
print('det(B) =', det(B))
print(f'k * det(A) = {k * det(A):.2f}')
print('Veificação: det(B) == k * det(A)? - ',np.isclose(det(B), k * det(A)))

# Propriedade 4: trocar duas linhas muda o sinal do determinante
print("\n========== 4) Troca de duas linhas inverte o sinal ==========")
C = A.copy()
C[[0, 1]] = C[[1, 0]] # Troca a linha 0 com a linha 1
print('Matriz C com linhas 1 e 2 trocadas:\n', C)
print('det(C) =', det(C))
print('det(A) =', det(A))
print('Verificação: det(C) == -det(A)?', np.isclose(det(C), -det(A)))

# Propriedade 5: matriz com duas linhas iguais → det = 0
print("\n========== 5) Duas linhas iguais => det = 0 ==========")
D = np.array([A[0], A[0], A[2]])
print('Matriz D com duas linhas iguais:\n', D)
print('det(D) =', det(D))

# Propriedade 6: det(A + B) != det(A) + det(B)
print("\n========== 6) det(A + B) != det(A) + det(B) ==========")
B = np.array([[0, 5, 4],
			  [8, 2, 1],
			  [9, -2, 3]])
print('Nova matriz B =\n', B)
print('A + B =\n', A + B)
print(f'det(A + B) = {det(A + B):.2f}')
print(f'det(A) + det(B) = {det(A) + det(B):.2f}')
print('Verificação: det(A + B) == det(A) + det(B)?',np.isclose(det(A + B), det(A) + det(B)))

# Propriedade 7: det(A @ B) = det(A) * det(B)
print("\n========== 7) det(A.B) = det(A) * det(B) ==========")
AB = A @ B
print('Produto A . B =\n', AB)
print(f'det(A . B) = {det(AB):.2f}')
print(f'det(A) * det(B) = {det(A) * det(B):.2f}')
print('Verificação: det(A.B) == det(A) * det(B)?', np.isclose(det(AB), det(A) *det(B))) # (*)

# (*) Verificações booleanas, comparação com np.isclose()







































