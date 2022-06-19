# Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes
# (os elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
# multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.

matA = []
matB = []

qtdLinhas = int(input('Digite a quantidade de linhas: '))
qtdColunas = int(input('Digite a quantidade de colunas: '))

for linha in range(qtdLinhas):
    linhaMatrizA = []
    linhaMatrizB = []
    for coluna in range(qtdColunas):
        numero = 0
        while numero <= 0:
            numero = int(input('Digite um número maior do que 0 para a matriz A: '))
        linhaMatrizA.append(numero)
        numero = 0
        while numero <= 0:
            numero = int(input('Digite um número maior do que 0 para a matriz B: '))
        linhaMatrizB.append(numero)
    matA.append(linhaMatrizA)
    matB.append(linhaMatrizB)

print(str(matA))
print(str(matB))