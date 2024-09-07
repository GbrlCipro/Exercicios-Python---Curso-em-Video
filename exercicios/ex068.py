# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
import time
from random import randint

numVit = 0

while True:
    numJog = int(input('Escolha seu número: '))
    numMaq = random.randint(0, 10)
    totNum = numJog + numMaq

    palpJog = str(input('Qual é o seu palpite? [P/I] ')).strip().upper()[0]
    while palpJog not in 'PI':
        palpJog = str(input('Qual é o seu palpite? [P/I] ')).strip().upper()[0]

    if palpJog == 'P':
        palpMaq = 'I'
    else:
        palpMaq = 'P'

    if totNum % 2 == 0:
        resultPalp = 'P'
        par = 'Par'
    else:
        resultPalp = 'I'
        impar = 'Ímpar'

<<<<<<< Updated upstream
    time.sleep(1)
    print('=' * 30)
    time.sleep(1)
    print('Processando a partida...')
    time.sleep(1)
=======
print('Escolha da maquina: ', numMaq)
print('Escolha do jogador: ', numJog)
print('Palpite da maquina: ', palpMaq)
print('Palpite do jogador: ', palpJog)
>>>>>>> Stashed changes

    print(f'\nNúmero do jogador: {numJog}')
    time.sleep(0.5)
    if palpJog == 'P':
        print('Palpite do jogador: Par')
    else:
        print('Palpite do jogador: Ímpar')
    time.sleep(1)

    print(f'\nNúmero da máquina: {numMaq}')
    time.sleep(0.5)
    if palpMaq == 'P':
        print('Palpite da máquina: Par')
    else:
        print('Palpite da máquina: Ímpar')
    time.sleep(1)

    # Verificação do resultado
    if resultPalp == 'P':
        print(f'\nO total dos números foi {totNum} e o resultado é {par}')
    else:
        print(f'\nO total dos números foi {totNum} e o resultado é {impar}')
    
    # Definir o vencedor
    if palpJog == resultPalp:
        vencedor = 'JOGADOR'
        numVit += 1
    else:
        vencedor = 'MÁQUINA'
    
    print(f'O vencedor foi {vencedor}\n')
    
    time.sleep(1)
    print('=' * 30)
    time.sleep(1)

    # Verificar condição de fim de jogo
    if vencedor == 'MÁQUINA':
        if numVit > 1:
            print(f'\nGAME OVER. Você venceu {numVit} vezes.')
        else:
            print(f'\nGAME OVER. Você venceu {numVit} vez.')
        time.sleep(1)
        break