# Jonatan Paschoal
# 12 de jul de 2025
# Plot de vetores 
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Função nativa para plotar  vetores 2D
def plotVectores(vecs, cols, alpha=1):
	plt.figure()
	plt.axvline(x=0, color='#A9A9A9', zorder=0)
	plt.axhline(y=0, color='#A9A9A9', zorder=0)

	for i in range(len(vecs)):
		x = np.concatenate([[0,0],vecs[i]])
		plt.quiver([x[0]],
			       [x[1]],
			       [x[2]],
			       [x[3]],
			       angles='xy', scale_units='xy', scale=1, color=cols[i],
			       alpha=alpha)

# Definindo as cores
laranja = '#FF9A13'
azul = '#1190FF'

# Chamando a função
plotVectores([[2,3], [4,-1]], [laranja, azul])

# Definindo o tamanho do plano cartesiano
plt.xlim(-5,5)
plt.ylim(-5,5)

# Plotando o gráfico
plt.show()