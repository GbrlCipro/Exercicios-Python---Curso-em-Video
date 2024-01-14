
# Crie um programa que faça o computador jogar Jokenpô com você.

'''import random

opcoes = ['Pedra', 'Papel', 'Tesoura']

escolha1 = random.choice(opcoes)
escolha2 = ''

while escolha2 not in opcoes:
    escolha2 = input('Escolha sua opção: Pedra, Papel, ou Tesoura: ').capitalize()
    if escolha2 not in opcoes:
        print('Opção inválida, as opções são: Pedra, Papel, ou Tesoura.')

if escolha1 == 'Papel' and escolha2 == 'Pedra':
    print('Máquina:', escolha1)
    print('Você:', escolha2)
    print('A máquina venceu, mais sorte na próxima vez!')
elif escolha1 == 'Tesoura' and escolha2 == 'Papel':
    print('Máquina:', escolha1)
    print('Você:', escolha2)
    print('A máquina venceu, mais sorte na próxima vez!')
elif escolha1 == 'Pedra' and escolha2 == 'Tesoura':
    print('Máquina:', escolha1)
    print('Você:', escolha2)
    print('A máquina venceu, mais sorte na próxima vez!')
elif escolha1 == escolha2:
    print('Máquina:', escolha1)
    print('Você:', escolha2)
    print('Empate, recomece o jogo.')
else:
    print('Máquina:', escolha1)
    print('Você:', escolha2)
    print('Você venceu, parabéns!')'''

# Método Guanabara

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida')
elif computador == 2:# Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')