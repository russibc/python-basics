# Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um
# dicionário, onde a chave é a vogal considerada.

dic = {}
word = input('Digite uma frase:\n')
ref = "aeiou"
k = 0
for i in range(len(word)):
    if word[i] in ref:
        if(word[i] not in dic):
            print('entro b')
            dic[word[i]] = 1
        else:
            k = dic[word[i]]
            k += 1
            dic[word[i]] = k

print(str(dic))