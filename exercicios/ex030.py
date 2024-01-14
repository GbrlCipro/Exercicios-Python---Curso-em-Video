
# Crie um programa que leia um número inteiro, e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'{num}\nO número digitado é par.')
else:
    print(f'{num}\nO número digitado é ímpar.')