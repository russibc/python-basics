# Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a
# chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome.
# Escreva uma função que retorna a média do aluno, dado seu nome.

def calcula_media(nome):
    return (dicionario[nome][0] + dicionario[nome][1]) / 2


def exibe_todas_as_medias():
    for aluno in dicionario:
        media = (dicionario[aluno][0] + dicionario[aluno][1]) / 2
        print('Média ' + f'{aluno}: {media}')


dicionario = {}
nome = 'xxx'
while (nome != '' or len(nome) != 0):
    nome = input("NOME DISCENTE:\n")
    if(nome != '' or len(nome) != 0 ):
        nota1 = float(input(f'NOTA 1 DISCENTE {nome}\n'))
        nota2 = float(input(f'NOTA 2 DISCENTE {nome}\n'))
        dicionario[nome] = (nota1, nota2)

exibe_todas_as_medias()
