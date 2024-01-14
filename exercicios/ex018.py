# Crie um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tângente
# desse ângulo

# Meu método

'''import math

graus = 45
angulo = math.radians(graus)
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f'Para um ângulo de {graus}º, temos:\nSeno: {sen:.3f}\nCosseno: {cos:.3f}\nTangente: {tan:.3f}')'''

# Método Guanabara

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,sen))
cos = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cos))
tan = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tan))
