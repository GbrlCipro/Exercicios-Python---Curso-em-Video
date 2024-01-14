
# A confederação nacional de natação, precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria de acordo com a
# sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - nasc

print('Idade: {}'.format(idade))

if idade <= 9:
    print('Esse atleta pertence à categoria MIRIM.')
elif idade <= 14:
    print('Esse atleta pertecen à categoria INFANTIL.')
elif idade <= 19:
    print('Esse atleta pertence à categoria JUNIOR.')
elif idade <= 20:
    print('Esse atleta pertence à categoria SÊNIOR.')
else:
    print('Esse atleta pertence à categoria MASTER.')
