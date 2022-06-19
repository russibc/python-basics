# Calcula a média móvel do tamanho da janela 3, para a matriz 1D fornecida.

import numpy as np

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

np.random.seed(100)

Z = np.random.randint(10, size=10)

print(moving_average(Z,4))