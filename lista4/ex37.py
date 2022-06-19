# De 2 arrays numpy, extraia os índices nos quais os elementos dos 2 arrays correspondem.

import numpy as np

arr1 = np.array([11, 12, 13, 14, 15, 16, 17])

arr2 = np.array([12, 13, 14, 18, 19, 20, 21])

result = np.intersect1d(arr1, arr2)

print(result)