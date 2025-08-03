# Jonatan Paschoal
# 02 de ago de 2025
# Determinante de matrizes em python
# Determinates - numpy.linalg, função para uso do (det)
# Uso matplotlib.pyplot
# Código com gráficos explicativos (para matrizes 2x2)
#
#-------------------------------------------
# Determinantes propriedades (Área do paralelogramo)

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import det

def plot_paralelogramo(M, title=''):
	origem = [0, 0]
	v1 = M[:, 0]
	v2 = M[:, 1]

	plt.figure(figsize=(6, 6))
	plt.quiver(*origem, *v1, angles='xy', scale_units='xy', scale=1, color='r', label='v1')
	plt.quiver(*origem, *v2, angles='xy', scale_units='xy', scale=1, color='b', label='v2')

	# Desenha o paralelogramo
	pts = np.array([[0, 0], v1, v1 + v2, v2, [0, 0]])
	plt.plot(pts[:, 0], pts[:, 1], 'g--', alpha=0.7)

	area = abs(det(M))
	plt.title(f'{title}\nDeterminante = {area:.2f}')
	plt.axis('equal')
	plt.grid(True)
	plt.axhline(0, color='gray', linewidth=0.5)
	plt.axvline(0, color='gray', linewidth=0.5)
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	plt.legend()
	plt.show()

# ===== MATRIZ ORIGINAL =====
A  = np.array([[2, 1],
			   [1, 3]])

print('Matriz A:\n', A)
print('det(A) =',det(A))
plot_paralelogramo(A, title='1) Matriz A')

# ===== TROCA DE LINHAS (mudança de sinal) =====
A_trocada = A[[1, 0], :]
print('\nMatriz A com linhas trocadas:\n',A_trocada)
print('det(A_trocada) =', det(A_trocada))
plot_paralelogramo(A_trocada, title='2) Troca de linhas: sinal do determinante muda')


# ===== MULTIPLICAÇÃO DE LINHA =====
k = 2
A_modificada = A.copy()
A_modificada[0, :] *= k
print(f'\nMatriz A com linha multiplicada por {k}:\n', A_modificada)
print('det(A_modificada) =', det(A_modificada))
plot_paralelogramo(A_modificada, title=f'3) Linha 1 multiplicada por {k}')


# ===== MATRIZ COM LINHAS IGUAIS =====
A_igual = np.array([[2, 1],
					[2, 1]])
print('\nMatriz com linhas iguais:\n', A_igual)
print('det =', det(A_igual))
plot_paralelogramo(A_igual, title='4) Duas linhas → Determinante = 0')
