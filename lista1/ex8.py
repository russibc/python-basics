# Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês,
# sem usar a fórmula de juros compostos. O usuário deve informar quanto será investido por mês e
# qual será a taxa de juros mensal. O programa deve informar o saldo do investimento após um ano
#  (soma das aplicações mês a mês considerando os juros compostos), e perguntar ao usuário se ele
#  deseja que seja calculado o ano seguinte sucessivamente. Por exemplo, caso o usuário deseje
# investir R$ 100,00 por mês, e tenha uma taxa de juros de 1% ao mês, o programa forneceria
# a seguinte saída:
#
# Saldo do investimento após 1 ano: R$ 1.268,25
# Deseja processar mais um ano? (S/N)

op = ''
saldo = 0

investimento = float(input('Informe o quanto você quer investir: '))
juros = float(input('Informe o valor dos juros mensais: '))

for item in range(12):
    saldo = investimento * (1 + juros/100)**12

print('Depois de um ano você terá: %.2f ' % saldo)

while(op != 'n'):

    op = input('Deseja calcular do ano seguinte? (s/n)\n')

    if(op == 's'):
        saldo = (saldo+investimento)*2 + juros/100
        print('O novo total é: %.2f' % saldo)
