
# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5, e peça para o usuário tentar adivinhar qual é esse número.
# O programa deverá exibir na tela se o usuário ganhou ou perdeu o desafio.

from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 5, pra você tentar advinhar')
num = str(randint(0,5))
palp = str(input('Qual é o seu palpite? '))
sleep(2)

if palp == num:
    print('O número que eu pensei foi {}, você ACERTOU!'.format(num))
else:
    print('O número que eu pensei foi {}, você ERROU!'.format(num))
