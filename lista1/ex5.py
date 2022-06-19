# Faça um programa para listar todos os divisores de um número ou dizer que o número é primo
# caso não existam divisores. Ao final, verifique se o usuário deseja analisar outro número.

def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    yield num

op = ''
while(op != 'n'):
    num = int(input('Insira um número: '))

    vet = list(divisores(num))
    if(len(vet) == 2):
        print('Número '+str(num)+' é primo')
    else:
        print(str(vet))

    op = input('Deseja analisar outro número? (Digite S ou N)\n')
    op = op.lower()
