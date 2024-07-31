# Crie um programa que leia vários números inteiros pelo teclado. No final mostre qual foi a média entre todos os valores, e quais foram o maior e o menor valor lido. O programa deve perguntar se o usuário quer continuar a digitar valores.


while True:
    somaNum = 0
    qtdNum = 0
    maiorNum = 0
    menorNum = 0
    num = int(input('Digite um número inteiro: '))
    while True:
        somaNum += num
        qtdNum += 1
        if num > maiorNum:
            maiorNum = num
        if num < menorNum:
            menorNum = num
        mediaNum = somaNum / qtdNum
        print('somaNum ', somaNum)
        print('qtdNum', qtdNum)
        print('maiorNum', maiorNum)
        print('menorNum', menorNum)
        print('mediaNum', mediaNum)
        resp = input('Gostaria de continuar digitando? [S/N] ')
        if resp in 'Ss':
            break