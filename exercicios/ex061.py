# Refaça o desafio 051, lendo o Primeiro Termo e a Razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while

contador = 0
primeiro = int(input('\nPrimeiro termo: \n'))
razao = int(input('Razão: \n'))

while contador < 10:

    print(primeiro)
    primeiro += razao
    contador += 1

    print('Deseja mostrar mais quantos termos? ')

    if resp == 0:
        break
    else:
        