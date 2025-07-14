# Jonatan Paschoal
# 13 de jul de 2025
# Plot de vetor 2D
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=0.5):
    ''' função para plotar vetores'''
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
#Cores
cor1 = '#FF0000'
cor2 = '#FF0000'
corRes = '#11FFFF'

# Vetores
a = np.array([2,3])
b = np.array([3,1])

# Soma
r =  a + b

# Função
plotVectors([a, b, r], [cor1, cor2, corRes])

# Plano cartesiano
plt.xlim(-1,6)
plt.ylim(-5,10)

plt.show()