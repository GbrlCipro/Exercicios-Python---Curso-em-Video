# Crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa devera perguntar se o usuario quer continuar ou nao . No final mostre:

# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.

import time

mais18 = 0
homem = 0
mulher20 = 0


while True:             # inicializando o loop que vai funcionar até que o usuário responda "Sim"    

    idade = int(input("Idade: "))

    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]  # Bloquinho pra capturar o sexo, e garantir que o usuario insira corretamente 
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
                        # Verficando quantas pessoas tem mais de 18 anos, e fazendo a contagem delas
    if idade > 18:
        mais18 += 1
                        # Verificando quantos homens foram listados, e fazendo a contagem deles
    if sexo == "M":
        homem += 1
                        # Verficando quantas mulheres tem menos de 20 anos, e fazendo a contagem delas
    if sexo == "F" and idade < 20:
        mulher20 +=1
                        # Verificando a resposta da pergunta: "Quer continuar?". Caso seja "N" de não, o programa breaka
    if resp == 'N':
        time.sleep(1)
        print('\nVocê escolheu sair, o programa vai ser encerrado.\n')
        time.sleep(1)
        print(f'Pesssoas com mais de 18 anos: {mais18}\nQuantidade de homens: {homem}\nQuantidade de mulheres com menos de 20 anos: {mulher20}\n')
        time.sleep(1)        
        break