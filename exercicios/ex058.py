# Melhore o jogo do DESAFIO 28, onde o computador vai "pensar" em um número de 0 a 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep

tentativas = 0

print('Vou pensar em um número entre 0 e 10, pra você tentar advinhar')
num = str(randint(0,10))

while True:
    palp = str(input('Qual é o seu palpite? '))
    sleep(2)

    if palp == num:
        print('O número que eu pensei foi {}, você ACERTOU! Tentativas: {}'.format(num, tentativas))
        break
    else:
        tentativas += 1
        print('O número não é esse, você ERROU!'.format(num))