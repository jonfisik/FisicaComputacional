# Jonatan Paschoal
# 12, 13 de jul de 2025
# Plot de vetores canônicos 3D
#-------------------------------------------

import numpy as np # Usado para manipulação dde vetores
import matplotlib.pyplot as plt # Biblioteca de gráficos
from mpl_toolkits.mplot3d import Axes3D # Suporte para gráficos 3D

# Definição canônica de vetores
e1 = np.array([1,0,0])
e2 = np.array([0,1,0])
e3 = np.array([0,0,1])

# Lista de vetore e cores
vetores = [e1, e2, e3] # Vetores agrupados em lista, para serem iterados
cores = ['r', 'g', 'b'] # vermelho (red), verde (green), azul (blue)

# Criar figuras e eixos 3D
fig = plt.figure() # Cria a figura 
ax = fig.add_subplot(111, projection='3d') # Define o gráfico 3D (111 - 1 linha, 1 coluna, 1° gráfico)

# Plotar os vetores
for i in range(len(vetores)): # Para percorrer os vetores
	ax.quiver(0, 0, 0,        # Origem -- ax.quiver usado para desenhar setas 3D
			  vetores[i][0],  # Componente x
			  vetores[i][1],  # Componente y
			  vetores[i][2],  # Componente z
			  color=cores[i], arrow_length_ratio=0.1) # color=cores[i], define a cor da seta

# Configuração dos eixos 
# Bloco define os limites de visualização para cada eixo (x,y,z)
# (label), define rótulos nos eixos e título
ax.set_xlim([0, 1.2])
ax.set_ylim([0, 1.2])
ax.set_zlim([0, 1.2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Vetores e1, e2, e3 em 3D')

# Gráfico
plt.show()