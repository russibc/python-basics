# Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a
# soma das matrizes A e B.

matA = []
matB = []
matC = []

for linhas in range(2):
    linha = []
    for colunas in range(2):
        linha.append(
            eval(input("Digite um número[" + str(linhas) + "," + str(colunas) + "]: ")))
    matA.append(linha)

for linhas in range(2):
    linha = []
    for colunas in range(2):
        linha.append(
            eval(input("Digite um número[" + str(linhas) + "," + str(colunas) + "]: ")))
    matB.append(linha)

for linhas in range(2):
    linha = []
    for colunas in range(2):
        linha.append(matA[linhas][colunas] + matB[linhas][colunas])
    matC.append(linha)

print(str(matA))
print(str(matB))
print(str(matC))


