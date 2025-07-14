# Jonatan Paschoal
# 13 de jul de 2025
# Plot da combinação linear de vetores canônicos 3D
# Passo a passo da combinação linear.
# Criando arquivo .gif
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Vetores base canônica e combinação linear
e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])
v = 2*e1 + 1*e2 + 3*e3

# Vetores e cores
vetores = [2*e1, e2, 3*e3, v]
cores = ['r', 'g', 'b', 'k']
labels = ['2e1', 'e2', '3e3', 'v = 2e1 + e2 + 3e3']

# Criar figura e eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar todos os vetores (fixos)
for  i in range(len(vetores)):
	ax.quiver(0, 0, 0,
			  vetores[i][0],
			  vetores[i][1],
			  vetores[i][2],
			  color=cores[i],
			  label=labels[i],
			  arrow_length_ratio=0.1)

# Limites dos eixos
ax.set_xlim(0, 3)
ax.set_ylim(0, 2)
ax.set_zlim(0, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Vetores em 3D com rotação da câmara')
ax.legend()

# Função de animação: rotaciona a câmera
def update(frame):
	ax.view_init(elev=20, azim=frame) # ângulo (azimutal) horizontal (graus), controla a perspectiva da câmera
	return []

# Criar animação (Rotacionando de 0 a 360 graus)
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False)

# Salvar como gif
#ani.save("rotacao_camera.gif", writer='pillow', fps=20)

# Mostrar o gráfico (opcional, se quiser rodar na tela também)
plt.show()