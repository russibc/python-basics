# Escreva um programa que declare um vetor com 10 valores inteiros predefinidos.
# O programa deverá ler um valor inteiro e informar se o valor se encontra no vetor e,
# em caso afirmativo, em qual(is) posição(ões) o valor foi encontrado.
# Ao final, o programa deverá ordenar o vetor em ordem decrescente e escrever todos os valores na tela.

encontrado = False
atual = []
vetor = [80, 10, 15, 20, 35, 10]

leitura = int(input('Insira um valor: '))

for i in range(len(vetor)):
    if leitura == vetor[i]:
        encontrado = True
        atual.append(i)

if(encontrado == False):
    print('Valor não se encontra no vetor')

print('Valor encontrado na(s) posição(ões): '+ str(atual))
vetor.sort(reverse=True)
print('Vetor em ordem decrescente: ' + str(vetor))
