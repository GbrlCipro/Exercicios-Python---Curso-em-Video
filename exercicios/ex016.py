# Crie um programa que leia um número real, e mostre na tela
# sua porção inteira DICA : MÓDULO MATH
'''
from math import trunc

n = float(input('Digite um número '))
print('O valor digitado é {}, e sua parte inteira é {}'.format(n, trunc(n))) # math.floor() retorna apenas a parte inteira de um número

# Aqui importamos apenas o método trunc() da biblioteca math, economizando assim
# memória do computador
'''

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(n, int(n)))

# Aqui consiguimos o mesmo resultado, utilizando uma função interna que dispensa a
# importação de qualquer biblioteca