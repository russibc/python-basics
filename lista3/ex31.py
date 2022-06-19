# Faça uma função que receba dois números A e B. Verifique se A possui divisão inteira por B
# (por meio de uma função), caso não seja, troque os valores de A por B e de B por A,
# (por meio de uma outra função) e verifique novamente se são divisíveis.

def checa_inverte_divisibilidade(a, b):
    if((b % a) == 0):
        print(str(a) + ' NÃO é divisível por '+str(b))
        print('Mas ' + str(b) + ' é divisível por '+str(a))
        return True
    else:
        return False


def checa_divisibilidade(a, b):
    if((a % b) == 0):
        print(str(a) + ' é divisível por '+str(b))
        return True
    else:
        return checa_inverte_divisibilidade(a, b)


a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))

checa_divisibilidade(a, b)
