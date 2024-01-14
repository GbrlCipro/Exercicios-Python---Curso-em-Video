# Faça um programa que leia o peso de 5 pessoas, e no final mostre qual foi o maior e o menor peso lidos

maior_peso = 0
menor_peso = 0

for item in range(1, 6):
    peso = float(input('Digite o peso do paciente: '))
    if item == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso lido foi {maior_peso}')
print(f'O menor peso lido foi {menor_peso}')
