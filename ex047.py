# Crie um programa que mostre na tela todos os numeros pares, que estao no intervalo entre 1 e 50

print('\nOs números pares entre 1 e 50 são: ')

for n in range(1,50):
    if n % 2 == 0:
        print(n)
