# Escreva um programa que leia um número inteiro n e mostre na telas os n primeiros elementos de uma sequência de fibonacci

n = int(input('Quantos termos você quer mostrar? '))  # Solicita a quantidade de termos
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')  # Exibe os dois primeiros termos
cont = 3

while cont <= n:  # Corrige a condição do loop para contar até n
    t3 = t1 + t2
    print(f'> {t3}', end='')  # Exibe o próximo termo
    t1 = t2
    t2 = t3
    cont += 1  # Incrementa o contador para acompanhar o número de termos exibidos

print(' FIM')  # Adiciona 'FIM' ao final
