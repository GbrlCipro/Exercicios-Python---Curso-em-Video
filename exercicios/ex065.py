# Crie um programa que leia vários números inteiros pelo teclado. No final mostre qual foi a média entre todos os valores, e quais foram o maior e o menor valor lido. O programa deve perguntar se o usuário quer continuar a digitar valores.

somaNum = 0
qtdNum = 0
maiorValor = 0
menorValor = 0
mediaNum = somaNum / qtdNum


while True:
    n = int(input('Digite um número inteiro: '))

    if n != 999:
        somaNum += n
        qtdNum += 1
    else:   
        break


print(f"Foram digitados {qtdNum} números, e a soma deles é {somaNum} ")
print('A media dos numeros digitados é ', mediaNum)