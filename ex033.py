
# Faça um programa que leia 3 números, e mostre qual é o maior e qual é o menor

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

lista = [n1,n2,n3]
lista.sort() # Ordena os elementos de uma lista em ordem crescente.

print(f'O menor numero da lista é {lista[0]}, e o maior é {lista[-1]}')