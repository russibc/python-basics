# Faça um programa que leia duas matrizes A e B de números inteiros e verifica se ambas
# são inversas (ou seja, se a multiplicação de A por B é a matriz identidade).

a = []
b = []
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

for linha in range(qtdLinhas):
    linhaMatA = []
    linhaMatB = []
    for coluna in range(qtdColunas):
        numero = 0
        while numero <= 0:
            numero = (
                int(input("Digite um número maior do que 0 para a matriz A: ")))
        linhaMatA.append(numero)
        numero = 0
        while numero <= 0:
            numero = (
                int(input("Digite um número maior do que 0 para a matriz B: ")))
        linhaMatB.append(numero)

    a.append(linhaMatA)
    b.append(linhaMatB)

print(str(a))
print(str(b))
