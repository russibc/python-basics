# Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
# o maior elemento da matriz e sua respectiva posição (linha e coluna)
# o menor elemento da matriz e sua respectiva posição.

mat = []

maiorLinhaPos = 0
maiorColPos = 0
menorEl = 0
maiorEl = 0
menorLinhaPos = 0
menorColPos = 0

for linha in range(6):
    linhaMatriz = []
    for coluna in range(3):
        linhaMatriz.append(int(input('Digite um número: ')))

        if linha == 0 and coluna == 0:
            maiorEl = linhaMatriz[coluna]
            menorEl = linhaMatriz[coluna]
            maiorLinhaPos = linha
            maiorColPos = linha
            menorLinhaPos = coluna
            menorColPos = coluna
        else:
            if linhaMatriz[coluna] > maiorEl:
                maiorEl = linhaMatriz[coluna]
                maiorLinhaPos = linha
                maiorColPos = coluna
            if linhaMatriz[coluna] < menorEl:
                menorEl = linhaMatriz[coluna]
                menorLinhaPos = linha
                menorColPos = coluna
    mat.append(linhaMatriz)

print('Matriz: ')
print(str(mat))
print('Maior elemento: ' + str(maiorEl) + ' - Linha: ' +
      str(maiorLinhaPos) + ' - Coluna: ' + str(maiorColPos))
print('Menor elemento: ' + str(menorEl) + ' - Linha: ' +
      str(menorLinhaPos) + ' - Coluna: ' + str(menorColPos))
