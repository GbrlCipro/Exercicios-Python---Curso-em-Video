# Refaça o desafio 009 mostrando a tabuada de um numero que o usuario escolher,
# so que agora utilizando um laço for


numero = int(input('\nDigite um número para ver sua tabuada: '))
mult = 1

for n in range(0,10):
    res = numero * mult
    print(f'{numero:2} x {mult:2} = {res}')
    mult = mult + 1