# Jonatan Paschoal
# 13 de ago de 2025
# Sistemas Lineares
# Com entrada do usuário
# Método da eliminação de Gauss
#
#-------------------------------------------
# Sistema linear de qualquer ordem

import numpy as np

# ==== Entrada ====
n = int(input('Digite a dimensão da matriz A: '))

A = np.zeros((n ,n), dtype=float)
b = np.zeros(n, dtype=float)

# Matriz
print('\nDigite os elementos da matriz A: ')

for i in range(n):
	for j in range(n):
		A[i, j] = float(input(f'A[{i+1}][{j+1}]: '))

# Termos independentes
print('\nDigite os elementos do vetor b: ')

for i in range(n):
	b[i] = float(input(f'b[{i+1}]: '))

# === Monta matriz aumentada ===
M = np.hstack([A, b.reshape(-1, 1)])

# === Eliminação de Gauss ===
for k in range(n - 1):
	# Pivotamento parcial
	max_row = np.argmax(abs(M[k:, k])) + k
	if max_row != k:
		M[[k, max_row]] = M[[max_row, k]]

	for i in range(k + 1, n):
		fator = M[i, k] / M[k, k]
		M[i, k:] -= fator * M[k, k]

# === Substituição regressiva ===
x = np.zeros(n, dtype=float)
for i in range(n - 1, -1, -1):
	x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:])) / M[i, i]

# ==== Saída ====
print('\nSolução do sistema Ax = b: ')
for i in range(n):
	print(f'x[{i+1}] = {x[i]:.6f}')