
'''
Faça um programa que leia um número de 0 a 9999, e mostre na tela cada um dos seus
dígitos separados. Ex:

Numero -> 1834
Unidade -> 4
Dezena -> 3
Centena -> 8
Milhar -> 1
'''

num = int(input('Digite um número inteiro entre 0 e 9999: '))

un = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10

print(f'O número digitado foi {num}\nUnidade: {un}\nDezena: {dez}\nCentena: {cen}\nMilhar: {mi}')
