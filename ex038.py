
# Escreva um programa que leia dois números inteiros, e compare-os,
# mostrando na tela uma mensagem:
# O primeiro valor é o maior;
# O segundo valor é o maior;
# Não existe um valor maior, os dois são iguais

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Nenhum valor é maior, ambos são iguais.')