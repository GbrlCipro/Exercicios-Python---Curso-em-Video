# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se ele é primo: '))
num_div = 0

for c in range(1, (num + 1)):
    if num % c == 0:
        num_div += 1

if num_div == 2:
    print('É um número primo.')
else:
    print('Não é um número primo.')
