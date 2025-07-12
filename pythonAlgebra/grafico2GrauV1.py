# Jonatan Paschoal
# 12 de jul de 2025
# Gráfico da eq. 2 grau
#-------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

x = np.array(np.linspace(-100,100,50))
y = x**2

print(x)
print(y)

plt.plot(x,y)
plt.show()
