# Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal
# principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

matriz = []

for linha in range(3):
    linhaMatriz = []
    for coluna in range(3):
        linhaMatriz.append(int(input("Digite um número: ")))
    matriz.append(linhaMatriz)

print(str(matriz))

k = int(input("Digite um número k: "))

for linha in range(3):
    for coluna in range(3):
            if linha == coluna:
                matriz[linha][coluna] = k * matriz[linha][coluna]

print(str(matriz))