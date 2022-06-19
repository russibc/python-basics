# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
# uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso
# a data seja inválida.
import datetime

formato = '%d/%m/%Y'
meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
           7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

def valida_data(data):
    try:
        datetime.datetime.strptime(data, formato)
        return True
    except ValueError:
        print("Formato incorreto.")
        return False

def formata_data(data):
    if(valida_data(data) == True):
        dia, mes, ano = data.split("/")
        return str(dia) + ' de ' + meses[int(mes)] + ' de ' + str(ano)
    else:
        return False

result = False
while(result == False):
    data = input('Insira uma data no formado dd/mm/aaaa (exemplo: 01/01/2020): ')
    result = formata_data(data)
    if(result != False):
        print(result)
