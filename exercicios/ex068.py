import random
import time

numVit = 0

while True:
    numJog = int(input('Escolha seu número (0 a 10): '))
    numMaq = random.randint(0, 10)
    totNum = numJog + numMaq

    palpJog = str(input('Qual é o seu palpite? [P/I] ')).strip().upper()[0]
    while palpJog not in 'PI':
        palpJog = str(input('Palpite inválido! Qual é o seu palpite? [P/I] ')).strip().upper()[0]

    if palpJog == 'P':
        palpMaq = 'I'
    else:
        palpMaq = 'P'

    if totNum % 2 == 0:
        resultPalp = 'P'
        resultado = 'Par'
    else:
        resultPalp = 'I'
        resultado = 'Ímpar'

    time.sleep(1)
    print('=' * 30)
    time.sleep(1)
    print(f'Você escolheu {numJog} e a máquina escolheu {numMaq}. Total é {totNum}, que é {resultado}.')
    time.sleep(1)

    # Definir o vencedor
    if palpJog == resultPalp:
        print('Você venceu!')
        numVit += 1
    else:
        print('A máquina venceu!')
        break

    print('=' * 30)
    time.sleep(1)

# Fim do jogo
if numVit > 1:
    print(f'\nGAME OVER. Você venceu {numVit} vezes consecutivas.')
else:
    print(f'\nGAME OVER. Você venceu {numVit} vez.')
