# Jonatan Paschoal
# 03 de ago de 2025
# Matrizes inversas em python (inv)
#
#-------------------------------------------
# Matrizes Inversas


import numpy as np
from numpy.linalg import det, inv

"""Função define se a matriz tem inv"""
def verificar_inversa(M, nome='Matriz'):
	print('=' * 50)
	print(f'{nome} = \n{M}') # Formatação f-strings
	d = det(M)
	print(f'\ndet({nome}) = {d:.2f}') # Formatação f-strings e arredondamento

	if np.isclose(d, 0):
		print(f'⚠️ {nome} é singular e não possui inversa.')
	else:
		inv_M = inv(M)
		print(f'\nInversa de {nome} =\n{np.round(inv_M, 3)}')

		identidade = M.dot(inv_M)
		print(f'\n{nome} x {nome}⁻¹ =\n{np.round(identidade, 3)}')

		if np.allclose(identidade, np.eye(M.shape[0])):
			print('✅ Verificação: A inversa está correta (A·A⁻¹ = I).')
		else:
			print('⚠️ Algo está errado: não obtivemos a matriz identidade.')

# ===== MATRIZ A =====
A = np.array([[1, -7, 2],
			  [4, 2, 7],
			  [1, 4, -1]])

verificar_inversa(A, nome='A')

# ===== MATRIZ B =====
B = np.array([[1, 1, 2],
			  [1, 1, 2],
			  [3, -1, -1]])

verificar_inversa(B, nome='B')