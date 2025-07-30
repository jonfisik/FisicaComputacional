# Jonatan Paschoal
# 30 de jul de 2025
# Determinante de matrizes em python
# Determinates com entrada de listas
#
#-------------------------------------------
# Determinantes

import numpy as np

# Entrada da matriz
entrada = input('Digite a matriz (como lista de listas, ex: [[1,2],[3,4]]): ')

# String para matriz 
try:
	# Matriz 
	A = np.array(eval(entrada))
	print('Matriz A = \n', A)

	# Cálculo do determinante
	det_A = np.linalg.det(A)
	print('Det(A) = ', np.round(det_A, 2)) # Arredonda parar duas casas decimais

except:
	print('Entrada inválida. Use a sintaxe correta.')