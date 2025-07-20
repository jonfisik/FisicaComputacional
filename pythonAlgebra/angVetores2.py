# Jonatan Paschoal
# 20 de jul de 2025
# Plot de ângulos entre vetores 
# 
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
	"""plota vetores"""
	for i in range(len(vecs)):
		plt.quiver(0, 0,                  # origem
				   vecs[i][0], vecs[i][1],# componentes do vetor (x,y)
				   angles='xy',scale_units='xy', scale=1, color=cols[i],
				   alpha=alpha)

# Ângulo entre vetores
def ang_2vetores(v, u):
	v_escalar_u = np.dot(v, u)
	vn = np.linalg.norm(v)
	un = np.linalg.norm(u)
	r = v_escalar_u / (vn * un)
	ang = np.arccos(r)

	return (180 / np.pi)*ang

# Vetores em R²
u = np.array([0, 1])
v = np.array([1, 0])

# Cores
red = 'red'
blue = 'blue'

# Plot
plt.figure()
plt.axvline(x=0, color='#A9A9A9', zorder=0)
plt.axhline(y=0, color='#A9A9A9', zorder=0)
plotVectors([u, v], [red, blue])
plt.xlim(-1, 1.5)
plt.ylim(-1, 1.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.title(f"Ângulo entre vetores = {ang_2vetores(u, v):.1f}°")
plt.show()