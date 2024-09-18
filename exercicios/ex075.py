# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3;
# C) Quais foram os números pares.

import random as rd
lista=[]
n=0
qtd9=0
par=0
pos3=0
while n < 4:
    num=int(input('Numero'))
    lista.append(num)
    if num == 9:
        qtd9+=1
    if num == 3:
        pos3=lista.index(3)
    else:
        pass
    if num%2==0:
        par+=1
    n+=1
tupla=tuple(lista)

print(f'Tupla com as entradas: {tupla}\nQuantidade de números "9": {qtd9}\nPosição do primeiro número 3: {pos3}\nQuantidade de números pares: {par}')