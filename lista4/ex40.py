# Adiciona um array de uma sequência não contínua de datas. Converta-o em uma sequência contínua de datas, 
# preenchendo as datas que faltam.

import numpy as np

dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 1)

print(dates)