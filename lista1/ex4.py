# Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado
# ao quadrado) e informe a sua classificação

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 17:
    print("Muito abaixo do peso")
elif imc > 17 and imc <= 18.49:
    print("Abaixo do peso")
elif imc > 18.50 and imc <= 24.99:
    print("Peso normal")
elif imc > 25 and imc <= 29.99:
    print("Acima do peso")
elif imc > 30 and imc <= 34.99:
    print("Obesidade I")
elif imc > 35 and imc <= 39.99:
    print("Obesidade II (severa)")
elif imc > 40:
    print("Obesidade III (mórbida)")
