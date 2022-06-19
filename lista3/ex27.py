# Faça um programa que, a partir de uma função que receba 3 números, retorne os 3 números ordem crescente.

def bubble_sort(arr):
    n = arr
    for passnum in range(len(n)-1,0,-1):
        for i in range(passnum):
            if n[i]>n[i+1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
    return n

n = [90,5,95]
print(bubble_sort(n))