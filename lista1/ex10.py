# Faça um programa que simula uma calculadora que aceita as seguintes operações: soma, subtração,
# divisão e multiplicação. O programa inicia pedindo para o usuário escolher uma opção do menu:
# Somar
# Subtrair
# Dividir
# Multiplicar
# Sair

op = 999
n1 = 0
n2 = 0
resul = 0

while(op != 5):

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("5 - Sair")

    op = int(input("Insira a operação desejada: "))
    if(op!=5):
        n1 = int(input('Insira número 1:'))
        n2 = int(input('Insira número 2:'))

        if op == 1:
            resul = n1+n2
        elif op == 2:
            resul = n1-n2
        elif op == 3:
            resul = n1/n2
        elif op == 4:
            resul = n1*n2

        print(str(resul))
