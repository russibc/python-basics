# Faça um programa que calcule o número de dias corridos entre duas datas, para vários pares de datas, considerando a 
# possibilidade de ocorrência de anos bissextos, sendo que:
# A primeira data é sempre a mais antiga 
# O ano é fornecido com 4 dígitos 
# A data fornecida com ZERO dias é sinal para encerrar a execução.

from datetime import datetime

def diferenca_dias(d1, d2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")
    return abs((d2 - d1).days)

soma = 0
d1 = ''
while(d1 != '0'):
    d1 = input("Digite o dia mais antigo: ")
    if(d1 != '0'):
        m1 = input('Digite o mês mais antigo: ')
        a1 = input('Digite o ano mais antigo: ')

        d2 = input("Digite o dia mais recente: ")
        m2 = input('Digite o mês mais recente: ')
        a2 = input('Digite o ano mais recente: ')

        date1 = d1 + '/' + m1 + '/' + a1
        date2 = d2 + '/' + m2 + '/' + a2

        soma = soma + diferenca_dias(date1, date2)

        print('\n\nTemos ' , soma, ' dias corridos no total.')