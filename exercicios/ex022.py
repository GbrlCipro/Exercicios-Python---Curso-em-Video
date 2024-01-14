
'''
Crie um programa que leia o nome completo de uma pessoa, e mostre na tela:

- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo (sem considerar os espaços);
- Quantas letras tem somente o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip()
nome_dividido = nome.split()
print(f'Nome: {nome}')
print('Nome em maiúsculo: ', nome.upper())
print('Nome em minúsculo: ', nome.lower())
print('Quantidade de letras sem considerar os espaços: ',len(nome.replace(" ", "")))
print('O primeiro nome é {}, e possui {} letras.'.format(nome_dividido[0],len(nome_dividido[0])))
