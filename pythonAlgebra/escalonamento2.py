# Jonatan Paschoal
# 26 de jul de 2025
# Escalonamento de matrizes em python
# Método - eliminação de Gauss
# Transformando a matriz para a forma escalonada
# reduzida de linha (Gauss - Jordan)
# Funciona para qualquer matriz aumentada m×(n+1) com pivôs não nulos
#
#-------------------------------------------
# Escalonamento de matrizes

import numpy as np

# Matriz aumentada (sistema linear Ax = B)
M = np.array([[1, 4, 3, 1],
			  [2, 5, 4, 4],
			  [1,-3,-2, 5]], dtype=float) # dtype (data type = tipo de dado. Ex. int, float, complex, etc)

print('Matriz original: \n', M)

# Escalonamento (eliminação de Gauss)
n_linhas, n_colunas = M.shape

# Passo 1: eliminação abaixo da diagonal principal
for i in range(n_linhas):
	pivot = M[i, i]
	if pivot == 0:
		raise ValueError(f'Pivô zero na liha {i}, tente trocar as linhas para evitar divisão por zero.')
		# raise: instrução usada para lançar um erro (exceção) em Python (*)
		# (**)

	# Normaliza a linha atual (torna o pivô igual a 1)
	M[i, :] = M[i, :] / pivot # Transforma o pivô da linha atual (M[i, i]) em 1, dividindo toda a linha por esse valor
	print(f'\nLinha {i} normalizada (pivô = 1):\n', M)

	# Zera os elementos abaixo do pivô (linha i)
	for j in range(i+1, n_linhas):
		fator = M[j, i]
		M[j, :] = M[j, :] - fator * M[i, :] # Remove os valores abaixo do pivô, transformando-os em zero com a combinação linear apropriada
		print(f'\nZerando elemento M[{j},{i}] com fator {fator}:\n', M) 

# Passo 2: Zerando os elementos acima da diagonal
for i in range(n_linhas-1, -1, -1):
	for j in range(i-1, -1, -1):
		fator = M[j, i]
		M[j, :] = M[j, :] - fator * M[i, :] # Percorre as linhas de baixo para cima, zerando os termos acima do pivô da linha atual.
		print(f'\nRetro-substituindo elemento M[{j},{i}] com fator {fator}:\n', M)

print("\nMatriz final escalonada (forma reduzida):\n", M)




''' (*) Serve para interromper o programa quando algo dá errado
	 ou quando você quer sinalizar um erro específico.

	(**) ValueError é um tipo de exceção que ocorre quando você 
	fornece um valor inadequado para uma operação ou função.
'''
# np.round(M) - arredonda valores