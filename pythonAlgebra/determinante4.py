# Jonatan Paschoal
# 30 de jul de 2025
# Determinante de matrizes em python
# Determinates com entrada de listas
#
#-------------------------------------------
# Determinantes

import numpy as np
from numpy.linalg import det

def ler_matriz_quadrada():
	'''Lê matriz quadrada inserida pelo usuário.'''
	while True:
		try:
			n = int(input('Digite a ordem da matriz quadrada (ex.: 2 para 2x2x): '))
			if n <= 0:
				print('A ordem da matriz deve ser um número inteiro positivo.')
				continue
			break
		except ValueError:
			print('Entrada inválida. Digite um número inteiro.')

	matriz = []
	print(f'\nDigite os elementos da matriz linha por linha, separados por espaço: ')

	for i in range(n):
		while True:
			linha = input(f'linha {i+1}: ').strip()
			elementos = linha.split()
			if len(elementos) != n:
				print(f'Você precisa digitar exatamente {n} números.')
				continue
			try:
				linha_numeros = [float(x) for x in elementos]
				matriz.append(linha_numeros)
				break
			except ValueError:
				print('Todos os elementos devem ser números.')

	return np.array(matriz)

def calcular_determinante(matriz):
	'''Calcula o determinante de uma matriz'''
	return np.linalg.det(matriz)

def main():
	print('===CÁLCULO DO DETERMINANTE DE UMA MATRIZ ===\n')
	A = ler_matriz_quadrada()
	print('\nMatriz A: ')
	print(A)

	det = calcular_determinante(A)
	print('\nDeterminante de A: ')
	print(np.round(det, 2))


if __name__=="__main__":
	main()


