# Faça um programa que leia três coordenadas num espaço 2D e indique se formam um triângulo, 
# juntamente com o seu tipo (equilátero, isósceles e escaleno)
#
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

a = int(input("Insira o lado A: "))
b = int(input("Insira o lado B: "))
c = int(input("Insira o lado C: "))

if a == b == c:
    print("Equilátero")
elif a == b or b == c or c == a:
    print("Isósceles")
else:
    print("Escaleno")
