# Jonatan Paschoal
# 13 de jul de 2025
# Plot de vetor 2D
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

e1 = np.array([1, 0])
e2 = np.array([0, 1])

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

plotVectors([e1,e2],[cor1,cor2])

plt.xlim(-1,1.5)
plt.ylim(-1,1.5)

plt.show()