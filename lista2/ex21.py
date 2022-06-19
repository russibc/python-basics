# Faça um programa que leia uma matriz 3x3 que representa um tabuleiro de jogo da velha
# e indique qual posição deveria ser jogada para ganhar o jogo (se possível) ou ao menos
# evitar uma derrota.

tabuleiro = ['-' for _ in range(9)]

jogoAtivo = True
ganhou = None
jogadorAtual = 'X'

def imprimirTabuleiro():
    j = 1
    tab = [tabuleiro[i*3:(i+1)*3] for i in range(3)]
    for i in tab:
        print("| " + " | ".join(i) + " |" + f'      | {j} | {j+1} | {j+2} |')
        j += 3

def trocaVez(current_player):
    print('Vez de ' + current_player)
    valido = True
    while valido:
        pos = input("Escolha um número de 0 a 9 (conforme posição do tabuleiro): ")
        while pos not in [str(i) for i in range(10)]:
            pos = input("Escolha um número de 0 a 9: ")
        pos = int(pos) - 1
        if tabuleiro[pos] == '-':
            tabuleiro[pos] = current_player
            valido = False
        else:
            print("Posição já escolhida")
        imprimirTabuleiro()

def fimJogo():
    validaVitoria()
    validaEmpate()

def validaVitoria():
    global ganhou
    linhaVen = check_row_winner()
    colVenc = check_col_winner()
    empate = check_dig_winner()
    if linhaVen:
        ganhou = linhaVen
    elif colVenc:
        ganhou = colVenc
    elif empate:
        ganhou = empate
    else:
        ganhou = None

def check_row_winner():
    global jogoAtivo
    j = 0
    for i in range(3):
        if tabuleiro[j] == tabuleiro[j+1] == tabuleiro[j+2] != '-':
            jogoAtivo = False
            return tabuleiro[j]
        j += 3

def check_col_winner():
    global jogoAtivo
    j = 0
    for i in range(3):
        if tabuleiro[j] == tabuleiro[j+3] == tabuleiro[j+6] != '-':
            jogoAtivo = False
            return tabuleiro[j]
        j += 1
    return None

def check_dig_winner():
    global jogoAtivo
    dig1 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != '-'
    dig2 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != '-'
    if dig1 or dig2:
        jogoAtivo = False
    if dig1:
        return tabuleiro[0]
    elif dig2:
        return tabuleiro[2]
    else:
        return None

def validaEmpate():
    global jogoAtivo
    if ganhou == None and '-' not in tabuleiro:
        jogoAtivo = False

def trocaJogador():
    global jogadorAtual
    jogadorAtual = 'X' if jogadorAtual == 'O' else 'O'


imprimirTabuleiro()
while(jogoAtivo):
    trocaVez(jogadorAtual)
    fimJogo()
    trocaJogador()

if ganhou == None:
    print("Empate")
else:
    print(f"{ganhou} ganhou!")