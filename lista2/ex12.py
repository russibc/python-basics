# Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos 
# valores diferentes existem no vetor.

vetor = []
cont = 10;
while(cont != 0):
    num = int(input('Insira um número: '))
    vetor.append(num)
    cont -= 1;

qtdNumIguais = 0
for i in range(len(vetor)):
    if((i+1) != len(vetor)):
        atual = vetor[i]
        if(atual==vetor[i+1]):
            qtdNumIguais += 1

print('Números diferentes: '+ str(len(vetor)-qtdNumIguais))