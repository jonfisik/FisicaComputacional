# Jonatan Paschoal
# 13 de jul de 2025
# Plot da combinação linear de vetores canônicos 3D
# Passo a passo da combinação linear.
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Vetores base canônica
e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])

# Vetores escalados
v1 = 2*e1 #2e1
v2 = 1*e2 #1e2
v3 = 3*e3 #3e3

# Soma total
v_total = v1 + v2 + v3

# Lista com etapas da soma
somas = [v1, v1 + v2, v1 + v2 + v3]

# Cores para os vetores
cores = ['r', 'g', 'b']
labels = ['2e1', '+e2', '+3e3']

# Criar figura e eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Limites dos eixos
ax.set_xlim(0, 3)
ax.set_ylim(0, 2)
ax.set_zlim(0, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Construção da combinação linear: 2e1 + e2 + 3e3')


# Vetores que serão desenhados dinamicamente
quivers = []

#Desenha uma seta a partir da origem até origem + vetor
def desenha_vetor(origem, vetor, cor, label=None):
	return ax.quiver(origem[0], origem[1], origem[2],
					 vetor[0], vetor[1], vetor[2],
					 color=cor, label=label, arrow_length_ratio=0.1)

def init():
	# Começa-se com nada
	return []

def update(frame):
	# Limpa vetores anteriores (não sobrepor)
	global quivers
	for q in quivers:
		q.remove()
	quivers = []

	origem = np.array([0, 0, 0])


	# Mostra os vetores um a um 
	if frame >= 0:
		quivers.append(desenha_vetor(origem, v1, 'r', '2e1'))
	if frame >= 1:
		origem = v1
		quivers.append(desenha_vetor(origem, v2, 'g', 'e2'))
	if frame >= 2:
		origem = v1 + v2
		quivers.append(desenha_vetor(origem, v3, 'b', '3e3'))
	if frame >= 3:
		# Vetor total desde a origem
		quivers.append(desenha_vetor(np.array([0, 0, 0]), v_total, 'k', 'v = 2e1+2e+3e3'))
	
	# Mostra legenda
	ax.legend()

	return quivers

# Animação com 4 frames
ani = FuncAnimation(fig, update, frames=4, init_func=init, interval=1000, blit=False, repeat=False)

# Mostrar o gráfico
plt.show()