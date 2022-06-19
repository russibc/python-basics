# Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
# Faça um programa que determine o percentual de ocorrências de face 6 do dado 
# dentre esses 50 lançamentos.

import random

print("Lançando dado 50 vezes...")

vet = [0]*50
qtdFaceSeis = 0
for jogada in range(len(vet)):
    vet[jogada] = random.randint(1, 6)
    if (vet[jogada] == 6):
        qtdFaceSeis = qtdFaceSeis+1

print("Verificando quantas vezes a face 6 apareceu...")
perc = (qtdFaceSeis/50)*100

print("\n ----- \n")
print("Valores: "+ str(vet))
print('Face 6 apareceu '+ str(qtdFaceSeis)+' vezes, ou seja, '+ str(perc)+'% das vezes')
