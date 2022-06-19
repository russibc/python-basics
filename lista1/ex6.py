#Faça um programa para determinar o número de dígitos de um número inteiro positivo informado.

sair = False
while(sair == False):
    numero = int(input('Insira um número inteiro e positivo: '))
    ehInteiro = isinstance(numero, int)
    if(ehInteiro):
        if(numero < 0):
            print('Número inserido não é positivo.')
        else:
            digitos = len(str(numero))
            print('A quantidade de dígitos do número inserido é: ' + str(digitos))
            sair = True
