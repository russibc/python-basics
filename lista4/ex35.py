# Converta um array 1-D em um array 3-D.

import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

array3d = array1d.reshape(2, 3, 2)

print(array3d)