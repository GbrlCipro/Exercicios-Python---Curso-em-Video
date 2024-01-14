
'''
Crie um programa que leia o nome de uma cidade, e diga se ela começa ou não com
o nome SANTO


cidade = str(input('Digite o nome da cidade: ').title().strip())
lista_cidade = cidade.split()

if lista_cidade[0] == 'Santo':
    print('A cidade {} começa com o nome "Santo"'.format(cidade))
else:
    print('A cidade {} não começa com o nome "Santo"'.format(cidade))
'''

cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid.split()[0].upper() == 'SANTO')