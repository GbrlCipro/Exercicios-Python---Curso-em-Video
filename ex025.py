
'''
Crie um programa que leia o nome de uma pessoa, e diga se ela tem SILVA no nome


nome = str(input('Digite o nome da pessoa: ')).title()

if 'Silva' in nome:
    print('Essa pessoa tem Silva no nome')
else:
    print('Essa pessoa não tem Silva no nome')
'''

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))