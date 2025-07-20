# Jonatan Paschoal
# 20 de jul de 2025
# Plot de ângulos entre vetores 
# 
#-------------------------------------------

import numpy as np # Biblioteca para Álgebra Linear
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
	"""Plot de vetores"""
	plt.figure()
	plt.axvline(x=0, color='#A9A9A9', zorder=0)
	plt.axhline(y=0, color='#A9A9B9', zorder=0)

	for i in range(len(vecs)):
		x = np.concatenate([[0,0], vecs[i]])
		plt.quiver([x[0]],
				   [x[1]],
				   [x[2]],
				   [x[3]],
				   angles='xy', scale_units='xy', scale=1, color=cols[i],
				   alpha=alpha)

# Ângulo entre vetores
def ang_2vetores(v, u):
  v_escalar_u = v.dot(u) # Produto escalar v.u -- vetor1.dot(vetor2)
  vn = np.linalg.norm(v) # Normal de v -- 
  un = np.linalg.norm(u) # Normal de u
  r = v_escalar_u / (vn*un) # cosseno do angulo
  ang = np.arccos(r) # ang em radianos (arccosseno)

  return (180/np.pi)*ang # ang em graus

  # Vetores em R2
u = np.array([0,1])
v = np.array([1,0])

red = 'red'
blue = 'blue'

plotVectors([u,v], [red, blue])
plt.xlim(-1,1.5)
plt.ylim(-1,1.5)

plt.gca().set_aspect('equal') # Deixar a escala uniforme nos eixos
plt.grid(True) # referência visual
plt.title(f"Ângulo entre vetores = {ang_2vetores(u, v):.1f}°")
plt.show()