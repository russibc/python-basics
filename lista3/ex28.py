# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

num = int(input("Insira um número inteiro positivo: "))  
num_invertido = 0    
def inverte_numero(num):  
    global num_invertido   
    if (num > 0):  
        aux = num % 10  
        num_invertido = (num_invertido * 10) + aux  
        inverte_numero(num // 10)  
    return num_invertido  
  
num_invertido = inverte_numero(num)  
print('Número inserido: '+str(num))
print('Número inserido invertido: '+str(num_invertido))