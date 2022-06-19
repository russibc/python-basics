# Crie uma função que retorne uma matriz identidade de dimensão N (parâmetro da função).
import numpy as np

def gera_identidade(n):
    return np.identity(n)

print(gera_identidade(3))