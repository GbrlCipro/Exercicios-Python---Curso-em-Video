
# Faça um programa que leia um ano qualquer e retorne se ele é BISSEXTO

from datetime import date

ano = int(input('Digite o ano: (coloque 0 para usar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
