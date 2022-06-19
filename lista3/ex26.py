# Faça um programa que receba as coordenadas x e y de três pontos, e a partir de uma função calcule
# a distância entre os pontos. Em uma outra função, verifique se os 3 pontos estão alinhados no plano 2D.
import math


def distancia_euclidiana2d(p1, p2, p3):
    d1 = math.dist(p1, p2)
    d2 = math.dist(p1, p3)
    d3 = math.dist(p2, p3)
    d = round((d1+d2+d3)/3, 2)
    return d


def confere_colinearidade2d(p1, p2, p3):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    print('Área: '+str(area))
    if(area == 0):
        res = True
    else:
        res = False
    return res


# coordenadas x, y
p1 = (1, 1)
p2 = (1, 4)
p3 = (1, 5)

print('Distância: ' + str(distancia_euclidiana2d(p1, p2, p3)))
print('São colineares? ' + str(confere_colinearidade2d(p1, p2, p3)))
