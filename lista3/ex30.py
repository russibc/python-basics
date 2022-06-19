# Faça uma função que receba uma lista de números armazenados de forma crescente,
# e dois valores (limite inferior e limite superior), e exiba a sublista cujos elementos
# são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.
# Exemplo:
# lista inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
# limite inferior = 13
# limite superior = 26
# lista exibida: [14,15,16,18,20,24,26]

cont = 0
lista3 = []
lista2 = []
lista1 = [12, 14, 15, 16, 18, 20, 24, 26, 28, 32, 34, 38]

print(str(lista1)+' <-- Lista')
print('Com base na lista acima...')
limite_inf = int(input('Insira a POSIÇÃO do limite inferior: '))
limite_sup = int(input('Insira a POSIÇÃO do limite superior: '))

for i in range(len(lista1)):
    if(lista1[i] >= limite_inf and lista1[i] <= limite_sup):
        lista3.append(lista1[i])
print('Lista nova: '+str(lista3))
