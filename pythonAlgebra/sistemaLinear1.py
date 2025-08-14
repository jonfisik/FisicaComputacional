# Jonatan Paschoal
# 13 de ago de 2025
# Sistemas Lineares
#
#
#-------------------------------------------
#

import numpy as np

# ==================================
# 1) Definição da matriz A e vetor b
# ==================================
# Exemplo: sistema
# 2x + y - z =  8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
# ==================================

''' A matriz dos coefientes, x vetor de incógnitas e
b vetor dos termos independentes '''

A = np.array([[2, 1, -1],
			  [-3, -1, 2],
			  [-2, 1, 2]])

b = np.array([8, 11, 2])

print('Matriz A (coeficientes):\n', A)
print("Vetor b (resultados):\n", b)

# ==============================================
# 2) Determinante para saber se há solução única
# ==============================================

det_A = np.linalg.det(A)
print('\nDterminante de A = ', det_A)

''' Se det(A) ≠ 0, existe solução única.
Se det(A) = 0, o sistema pode ser indeterminado (infinitas soluções)
ou incompatível (nenhuma solução). '''

if np.isclose(det_A, 0):
	print('O sistema pode ter infinitas soluções ou nenhuma')
else: 
	print('O sitema tem soulução única')

# ==============================
# 3) Resolvendo o sistema
# ==============================

try:
	x = np.linalg.solve(A, b) # Solução de A.x = b | x = np.linalg.solve(A, b) método direto para solução
	print('\nSolução do sistema (vetor x): \n', x)

	# Verificando A.x = b
	b_calc = A.dot(x)
	print('\nVerificação A.x\n', b_calc)

except np.linalg.LinAlgError as e:
	print('\nErro ao resolver: ', e)
