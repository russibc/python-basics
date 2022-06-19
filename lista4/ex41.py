# Faça uma função que encontre os k menores valores de um array NumPy

import numpy as np

arr = np.array([1,3,5,2,4,6])
print(arr)
k = 3
arr1 = np.sort(arr)
print(k, "Menores valores")
print(arr1[:k])
