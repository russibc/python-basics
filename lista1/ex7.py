#  Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo:
# 	F(0) = 0
# 	F(1) = 1
# 	F(n) - F(n-1) + F(n-2)

n1, n2 = 0, 1
i = 0
vet = []
num = 0
while(num <= 0):
    num = int(input("Insira um número inteiro e positivo: "))

    if num == 1:
        vet.append(n1)
    elif(num > 1):
        while i < num:
            vet.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            i += 1

print('Sequência Fibonacci de '+ str(num))
print(str(vet))
