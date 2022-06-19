# Faça um programa que solicite a entrada de N trabalhos de um aluno até que o usuário digite -1.
# O programa deve calcular e apresentar (através de uma função): a média final e o número de trabalhos
# inscritos.

def calcula_media(notas):
    soma = 0.0
    for i in range(len(notas)):
        soma += notas[i]
    return [soma / len(notas), len(notas)]

notaTrabalho = 0.0
notas = []
while (notaTrabalho != -1):
    notaTrabalho = float(input('Insira a nota do seu trabalho: '))
    if(notaTrabalho >= 0):
        notas.append(notaTrabalho)

result = calcula_media(notas)
media = result[0]
qtdNotas = result[1]
print(media)
print(qtdNotas)