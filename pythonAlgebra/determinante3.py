# Jonatan Paschoal
# 30 de jul de 2025
# Determinante de matrizes em python
# Definição da ordem
# 
#-------------------------------------------
# Determinantes

import numpy as np

# Entrada das linhas da matriz
n = int(input('Digite a ordem da matriz quadrada (ex. 3 para 3x3): '))

# inicialização de uma lista para as linhas da matriz
matriz = []

print('Digite os elementos linha por linha (separados por espaço): ')

for i in range(n):
	linha = input(f'Linha {i+1}: ')
	# Converte a linha de entrada em uma lista de inteiros
	linha_valores = list(map(float, linha.split()))
	if len(linha_valores) != n:
		print('Números incorreto de elementos. Tente novamente.')
		exit()
	matriz.append(linha_valores)

# Converte a lista de listas em array 
A = np.array(matriz)

# Exibir matriz
print('Matriz A=\n',A)

# Cálculo do determinante
det_A = np.linalg.det(A)
print('Det(A) = ',np.round(det_A,2))