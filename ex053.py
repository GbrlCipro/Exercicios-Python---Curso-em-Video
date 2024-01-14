# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase para verificar se ela é um palíndromo: ')).replace(' ', '')
frase_invertida = frase[::-1].replace(' ', '')

if frase == frase_invertida:
    print('A frase digitada É um palíndromo.')
else:
    print('A frase digitada NÃO é um palíndromo.')
