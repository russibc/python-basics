# Escreva um programa que leia 5 nomes (cadeia de caracteres)
# e 5 idades (inteiros) armazenando-os em 2 vetores. 
# Em seguida, o programa deverá escrever na tela o nome
# da pessoa mais velha e o nome da pessoa mais nova.

nomes = []
idades = []
for i in range(5):
    nome = input('Insira nome: ')
    nomes.append(nome)

    idade = int(input('Insira idade: '))
    idades.append(idade)

maior = 0
posMaior = 0
posMenor = 0
menor = 99
for i in range(len(idades)):
    if idades[i] > maior:
        maior = idades[i]
        posMaior = i

    if idades[i] < menor:
        menor = idades[i]
        posMenor = i

print('A maior idade é '+ str(maior) +' de '+str(nomes[posMaior]))
print('A menor idade é '+ str(menor) +' de '+str(nomes[posMenor]))

