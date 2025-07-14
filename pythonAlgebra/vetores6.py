# Jonatan Paschoal
# 13 de jul de 2025
# Plot da combinação de vetores canônicos 3D
# O vetor preto representa uma posição no espaço gerada pela combinação linear dos vetores da base.
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vetores canônicos
e1 = np.array([1,0,0])
e2 = np.array([0,1,0])
e3 = np.array([0,0,1])

# Combinação Linear: v = 2e1 + 1e2 + 3e3
v = 2*e1 + 1*e2 + 3*e3

# Lista de vetores e cores 
vetores = [e1, e2, e3, v]
cores = ['r', 'g', 'b', 'k']

# Criar figuras e eixos 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar figuras vetores e1, e2, e3 e v
for i in range(len(vetores)):
	ax.quiver(0, 0, 0,
		vetores[i][0],
		vetores[i][1],
		vetores[i][2],
		color=cores[i],
		arrow_length_ratio=0.1)

# Configuração dos eixos
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Combinação Linear: v = 2e1 + 1e2 + 3e3') 

# Mostrar o gráfico
plt.show()