# Jonatan Paschoal
# 12 de jul de 2025
# Produto escalar e módulo - vetores
#-------------------------------------------

import numpy as np

# Definição de vetores
u = np.array([2,3])
v = np.array([4,-1])

# Produto interno (escalar)
z = u.dot(v)

# Módulo dos vetores 'u' e 'v', função --> .norm(vetor)
modulo_u = np.linalg.norm(u) # foi atribuido o valor da norma a uma variável
modulo_v = np.linalg.norm(v) # Idem


# Resultado
print('u . v = ', z)

print('Modulo u = ', modulo_u)
print('Modulo v = ', modulo_v)