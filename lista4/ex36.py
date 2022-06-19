# Empilhe 2 arrays numpy horizontalmente, ou seja, 2 arrays que têm a mesma primeira dimensão
# (número de linhas em arrays 2D).

import numpy as np

a = np.array((1, 2, 3))
b = np.array((2, 3, 4))

print(np.column_stack((a, b)))
