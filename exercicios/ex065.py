# Crie um programa que leia vários números inteiros pelo teclado. No final mostre qual foi a média entre todos os valores, e quais foram o maior e o menor valor lido. O programa deve perguntar se o usuário quer continuar a digitar valores.

                                # Inicializando as variáveis que vão armazenar valores
maior = 0
menor = 0
qtd_num = 0
soma = 0
    
while True:                     #Iniciando o loop
                                # Registrando as entradas do usuário e alimentando os dados    
    num = int(input('\nDigite um número inteiro: '))        # Entrada do usuário
    qtd_num = qtd_num + 1       # Cada vez que um número é digitado, o contador aumenta em 1
    soma = soma + num           # Armazenando a soma dos números digitados
    media = soma / qtd_num      # Calculando a média dos números digitados

    if qtd_num == 1:            # Definindo o primeiro valor digitado como o menor número,
        menor = num             # para fazermos comparações posteriormente.
    if num > maior:             # Se o número digitado for maior que o maior número,
        maior = num             # o maior número recebe o número digitado
    elif num < menor:           # Se o número digitado for menor que o menor número, 
        menor = num             # o menor número recebe o número digitado
    else:                       # Caso não sejam maiores nem menores, eles são iguais
        pass                    # e nada acontece, apenas seguimos o código
    
    print('\nNumero digitado: ', num)
    print('\nsoma dos numeros digitados: ', soma)
    print('\nquantidade de números digitados: ', qtd_num)
    print('\nMédia dos números digitados: ', media)
    print('\nMaior número: ', maior)
    print('\nMenor número: ', menor)

    opcao = input('\nDeseja digitar outro número [S/N]: ') #  Capturando entrada do usuário

    if opcao in 'Ss':           # Se a opção estiver contida em Ss, o código prossegue
        pass
    elif opcao in 'Nn':         # Se a opção estiver contida em Nn, o código quebra
        break
    else:
        print('Digite apenas "S" ou "N"')   # Se não for nenhuma das outras opções o usuário
                                            # digitou a opção errada