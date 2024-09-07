# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$ 1000;
# C) Qual é o nome do produto mais barato.

import time

totalCompra = 0
prod1000 = 0
menorPreco = float('inf')
maisBarato = ''

while True:             # inicializando o loop que vai funcionar até que o usuário responda "Sim"

    produto = str(input('Produto: '))
    preco = float(input('Preço: '))

    if preco >= 1000:
        prod1000 += 1
    
    if preco < menorPreco:
        menorPreco = preco
        maisBarato = produto

    totalCompra += preco

                        # Verificando a resposta da pergunta: "Quer continuar?". Caso seja "N" de não, o programa breaka
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print(f'\nTotal gasto na compra: {totalCompra}\nQuantos produtos custaram mais de 1000,00 reais? {prod1000}\nO produto mais barato foi: {maisBarato}\n')
        time.sleep(1)
        print('\nVocê escolheu sair, o programa vai ser encerrado.\n')
        time.sleep(1)
        break