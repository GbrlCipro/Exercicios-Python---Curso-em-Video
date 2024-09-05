# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

vencedor = ''

palpJog = 'Par'
numJog = 1

palpMaq = random.randint(0, 1)
if palpMaq == 1:
    palpMaq = 'Impar'
else:
    palpMaq = 'Par'

numMaq = random.randint(1, 5)

resultNum = numJog + numMaq

print('Escolha da maquina: ', numMaq)
print('Escolha do jogador: ', numJog)

if resultNum % 2 == 0:
    resultNum = 'É PAR'
else:
    resultNum = 'É ÍMPAR'

print('Resultado: ', resultNum)

if palpJog == 'Impar' and resultNum == 'É ÍMPAR':
    vencedor = 'Jogador'
    print('O vencedor foi ', vencedor)
if palpJog == 'Par' and resultNum == 'É PAR':
    vencedor = 'Jogador'
    print('O vencedor foi ', vencedor)
elif palpMaq == 'Impar' and resultNum == 'É ÍMPAR':
    vencedor = 'Maquina'
    print('O vencedor foi ', vencedor)
elif palpMaq == 'Par' and resultNum == 'É PAR':
    vencedor = 'Maquina'
    print('O vencedor foi ', vencedor)
