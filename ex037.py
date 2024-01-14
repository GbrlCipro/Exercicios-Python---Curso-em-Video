
# Escreva um programa que leia um número inteiro, e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal
while True:

num = int(input('Digite um número: '))
lista_base = ['Binaria', 'Octal', 'Hexadecimal']
escolha = ''

while escolha not in lista_base:
    escolha = input('Pra que base deseja fazer a conversão do número? (Binária, Octal, ou Hexadecimal): ').strip().capitalize()
    if escolha not in lista_base:
        print('Opção inválida, por favor digite como apresentamos nas opções: ')

if escolha == 'Binaria':
    num_bin = bin(num)[2:] # Converter o número escolhido para base BINÁRIA
    print(f'O número {num} convertido para base {escolha} é: {num_bin}')
elif escolha == 'Octal':
    num_oct = oct(num)[2:] # Converter o número escolhido para base OCTAL
    print(f'O número {num} convertido para base {escolha} é: {num_oct}')
else:
    num_hex = hex(num)[2:] # Converter para a base HEXADECIMAL
    print(f'O número {num} convertido para base {escolha} é: {num_hex}')


