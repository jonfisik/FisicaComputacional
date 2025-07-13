# Jonatan Paschoal
# 12 de jul de 2025
# Plot de vetores 
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#
def plotVectors(vecs, cols, alpha=1):
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


laranja = '#FF9A13'
azul = '#1190FF'
#resultante = '#11FFFF'

#plotVectors([[2,3], [4,-1], [6,2]], [laranja, azul, resultante])
plotVectors([[2,3], [4,-1]], [laranja, azul])

plt.xlim(-1,7)
plt.ylim(-2,7)

plt.show()