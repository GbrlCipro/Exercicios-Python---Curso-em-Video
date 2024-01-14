
'''
Faça um programa que leia o nome completo de uma pessoa e mostre qual é o primeiro e o
último nome de forma separada
'''

n = str(input('Digite seu nome completo: ')).strip().title()

lista = n.split()

print('Primeiro nome {}'.format(lista[0]))
print('Último nome {}'.format(lista[-1]))