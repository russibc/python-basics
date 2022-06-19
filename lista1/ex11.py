# Faça um programa que leia dois vetores de 3 posições, que representam forças sobre um ponto no espaço 3D,
# e escreva a força resultante sobre esse ponto. A força resultante é obtida pela soma dos valores das 
# coordenadas correspondentes nos dois vetores: (x1 + x2), (y1+ y2), (z1 + z2).

vetorx = []
vetory = []
somax = 0
somay = 0

for i in range(3):
    valx = eval(input("Digite o valor de X"+str(i+1)+": "))
    vetorx.append(valx)
    somax += valx

for i in range(3):
    valy = eval(input("Digite o valor de Y"+str(i+1)+": "))
    vetory.append(valy)
    somay += valy

print('x1 + x2 + x3')
print(str(vetorx))
print(str(somax))

print('y1 + y2 + y3')
print(str(vetory))
print(str(somay))