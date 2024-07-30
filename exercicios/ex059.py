# Crie um programa que leia dois valores e mostre na tela um menu:
# 1 - Somar
# 2 - Multiplicar
# 3 - Maior
# 4 - Digitar novos números
# 5 - sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    num1 = int(input('\nDigite dois números\n\nPrimeiro número: '))
    num2 = int(input('Segundo número: '))

    while True:

        opcao = int(input('\nO que deseja fazer com esses números?\n\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Digitar novos números\n[5] - sair do programa\n\n'))

        if opcao == 1:
            somanum = int((num1 + num2))
            print(f'\nA soma dos números {num1} e {num2} é: {somanum}')
        elif opcao == 2:
            multnum = int(num1 * num2)
            print(f'\nO resultado da multiplicação de {num1} por {num2} é: {multnum}')
        elif opcao == 3:
            if num1 > num2:
                print(f'\nO maior número entre {num1} e {num2} é: {num1}')
            elif num1 < num2:
                print(f'\nO maior número entre {num1} e {num2} é: {num2}')
            else:
                print('\nOs números {num1} e {num2} são iguais.\n')
        elif opcao == 4:
            break
        elif opcao == 5:
            print('\nPrograma encerrado!\n')
            quit()
        else:
            print('\nOpção incorreta. Escolha apenas entre os números disponíveis\n')