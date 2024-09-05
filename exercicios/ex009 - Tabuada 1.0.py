# Faça um programa que leia um número inteiro qualquer, e exiba
# sua tabuada

n = int(input('Digite um numero para ver sua tabuada: '))
m = 1
print('-'*12)
print(f'Tabuada do {n}')
print()
while m < 11:
    r = (n * m)
    print(f'{n} X {m:2} = {r}')
    m = m + 1
print('-'*12)
