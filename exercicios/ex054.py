# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade, e quantas já são maiores.

from datetime import date

ano_atual = date.today().year # Cria uma variável que recebe o ano atual

maiores = 0
menores = 0

for c in range(0,2):
    ano_nasc = int(input('Qual é o ano de nascimento? '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f'Dos anos de nascimento, temos {maiores} maiores de idade, e {menores} menores de idade')