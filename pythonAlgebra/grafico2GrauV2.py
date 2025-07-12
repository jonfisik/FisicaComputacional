# Jonatan Paschoal
# 12 de jul de 2025
# Gráfico da eq. 2 grau
#-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Gerar Dados
x = np.linspace(-150, 100, 50)
y = x**2

# Criar figuras e eixos
plt.figure(figsize=(10,6))

# Plotar Dados
plt.plot(x,y, 'b-', linewidth=2) # Linha azul contínua


# Elementos Gráficos
plt.title("Parábola y = x²")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.5) # Linha do eixo x
plt.axvline(x=0, color='k', linestyle='-', alpha=0.5) # Linha do eixo y

# Mostrar gráfico
plt.show()