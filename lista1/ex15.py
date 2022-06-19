# Faça um programa que leia um vetor vet de 20 posições. O programa deve gerar, a partir do vetor lido,
# um outro vetor pos que contenha apenas os valores inteiros positivos de vet. A partir do vetor pos,
# deve ser gerado um outro vetor semdup que contenha apenas uma ocorrência de cada valor de pos.

vet = []
pos = []
semdup = []
item = 1
for item in range(20):
    item += 1
    num = int(input('Insira número '+ str(item)+': '))
    vet.append(num)
    

for w in range(len(vet)):
    vet[w] = float(vet[w])
    if vet[w] >= 0:
        pos.append(vet[w])
    while (vet[w] not in semdup) and (vet[w] >= 0):
        semdup.append(vet[w])

print("Vetor 'vet': "+str(vet))
print("Vetor 'pos': "+str(pos))
print("Vetor 'semdup': "+str(semdup))
