# Faça um programa que leia a largura e altura de uma parede em metros
# calcule sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta, pinta uma área de 2m²

alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
print(f'Altura: {alt:.2f}\nLargura: {lar:.2f}\nM²: {alt*lar:.2f}\nLitros de tinta necessários: {alt*lar/2:.2f}')
