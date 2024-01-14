# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa

# Meu método

'''from math import hypot

co = 3.5
ca = 4.75
print(f'Comprimento do cateto oposto {co}\nComprimento do cateto adjascente {ca}\nA hipotenusa vai medir {hypot(co, ca):.2f}') # math.hypot() calcula a hipotenusa baseado nos 2 valores que recebe como parâmetro, primeiro o cateto oposto, depois o cateto adjascente'''

# Método Guanabara SEM importação de bibliotecas

'''co = float(2)
ca = float(2.5)
h = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(h))'''

# Método Guanabara com importação

from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
