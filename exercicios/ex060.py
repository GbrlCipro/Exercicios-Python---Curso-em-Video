#Faça um programa que leia um número e mostre o seu fatorial

# Com While e com For


num = int(input('Digite um número: '))
cont = num
f = 1

print(f'Calculando {num}! => ', end = '')
while cont > 0:
    print(f'{cont}', end = '')
    print(' X ' if cont > 1 else ' = ', end = '')
    f *= cont
    cont -= 1
print(f'{f}')



# DEPOIS TENTAR FAZER COM WHILE