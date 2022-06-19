# Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em 
# que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, 
# o programa deve imprimir o valor -1.

encontrado = False
atual = []
vetor = []
for item in range(5):
    valor = int(input('Insira um número: '))
    vetor.append(valor)

valorBusca = int(input('Insira o valor que deseja buscar no vetor: '))

for i in range(len(vetor)):
    if valorBusca == vetor[i]:
        encontrado = True
        atual.append(i)

if(encontrado == False):
    print(-1)
else:
    print('Valor encontrado na(s) posição(ões): '+ str(atual))