# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).

somaNum = 0
qtdNum = 0

print('\nEsse programa vai retornar a soma de todos os números inteiros que você digitar. Para encerrar, digite o número 999.\n')

while True:
    n = int(input('Digite um número: '))

    if n != 999:
        somaNum += n
        qtdNum += 1
    else:   
        break

print(f"\nForam digitados {qtdNum} números, e a soma deles é {somaNum}\n")